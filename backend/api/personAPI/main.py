from fastapi import FastAPI, HTTPException, Query, Depends
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, Session
from sqlalchemy.ext.declarative import declarative_base
from dotenv import load_dotenv
from sqlalchemy_models import Person, Company, PersonCompany
from pydantic_models import PersonSchema
import os

load_dotenv()

SQLALCHEMY_DATABASE_URL = (
    "mysql+pymysql://root:" + os.getenv("DB_KEY") + "@localhost:3306/CNS-T3"
)
engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

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

    # convert ORM to Pydantic model
    person = persons[0]
    return PersonSchema(
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
