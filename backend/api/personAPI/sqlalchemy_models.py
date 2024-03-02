from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Boolean, Date, ForeignKey

Base = declarative_base()


class Person(Base):
    __tablename__ = "person"
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
    __tablename__ = "company"
    CompanyID = Column(Integer, primary_key=True)
    Name = Column(String(100))
    Industry = Column(String(25))
    CountryOfHeadquarters = Column(String(50))
    Type = Column(String(25))


class PersonCompany(Base):
    __tablename__ = "person_company"
    PersonID = Column(Integer, ForeignKey("Person.PersonID"), primary_key=True)
    CompanyID = Column(Integer, ForeignKey("Company.CompanyID"), primary_key=True)
    Role = Column(String(25))
