from fastapi import FastAPI, HTTPException, Query, Depends
from sqlalchemy import create_engine, Column, Integer, String, Boolean, Date, ForeignKey
from sqlalchemy.orm import sessionmaker, Session
from sqlalchemy.ext.declarative import declarative_base
from pydantic import BaseModel

SQLALCHEMY_DATABASE_URL = "mysql+pymysql://root:root@localhost:3306/CNS-T3"
engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()


# Define SQLAlchemy model for Person
class Person(Base):
    __tablename__ = "Person"
    PersonID = Column(Integer, primary_key=True)
    Name = Column(String(50))
    Occupation = Column(String(25))
    DoB = Column(Date)
    Nationality = Column(String(25))
    Description = Column(String(255))
    CountryOfResidency = Column(String(50))
    PEPStatus = Column(Boolean)
    SourceOfWealth = Column(String(25))
    ImgURL = Column(String(255))


class Company(Base):
    __tablename__ = "Company"
    CompanyID = Column(Integer, primary_key=True)
    Name = Column(String(100))
    Industry = Column(String(25))
    CountryOfHeadquarters = Column(String(50))
    Type = Column(String(25))


class PersonCompany(Base):
    __tablename__ = "Person-Company"
    PersonID = Column(Integer, ForeignKey("Person.PersonID"), primary_key=True)
    CompanyID = Column(Integer, ForeignKey("Company.CompanyID"), primary_key=True)
    Role = Column(String(25))


# Pydantic model for Person
class PersonOut(BaseModel):
    person_id: int | None
    name: str | None
    occupation: str | None
    dob: str | None
    nationality: str | None
    description: str | None
    company: str | None
    country_of_residency: str | None
    pep_status: str | None
    source_of_wealth: str | None
    img_url: str | None


app = FastAPI()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.get("/persons/search/")
async def search_persons_by_name(
    name: str = Query(None, min_length=1), db: Session = Depends(get_db)
):
    if not name:
        raise HTTPException(status_code=400, detail="Name parameter is required")

    # Search database for with name query
    persons = db.query(Person).filter(Person.Name.ilike(f"%{name}%")).all()
    if not persons:
        raise HTTPException(
            status_code=404, detail="No persons found with the provided name"
        )

    # get company and role
    companies = (
        db.query(Company)
        .join(PersonCompany)
        .filter(PersonCompany.PersonID == persons[0].PersonID)
        .all()
    )
    company = None
    if companies:
        company = companies[0].Name

    # convert ORM to pydantic model
    person = persons[0]
    person_out = PersonOut(
        person_id=person.PersonID,
        name=person.Name,
        occupation=person.Occupation,
        dob=person.DoB.strftime("%Y-%m-%d") if person.DoB else None,
        nationality=person.Nationality,
        description=person.Description,
        company=company,
        country_of_residency=person.CountryOfResidency,
        pep_status=person.PEPStatus,
        source_of_wealth=person.SourceOfWealth,
        img_url=person.ImgURL,
    )

    return person_out
