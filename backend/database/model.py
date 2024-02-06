from sqlalchemy import Column, Integer, String, Date, Boolean, ForeignKey
from database.database import Base

class Person(Base):
    __tablename__ = 'person'
    PersonID = Column(Integer, primary_key=True, autoincrement=True)
    Name = Column(String(50), nullable=False)
    DoB = Column(Date, nullable=False)
    CountryOfResidency = Column(String(50), nullable=False)
    Nationality = Column(String(25), nullable=False)
    Occupation = Column(String(25), nullable=False)
    PEPStatus = Column(Boolean)
    SourceOfWealth = Column(String(25))

class Company(Base):
    __tablename__ = 'company'
    CompanyID = Column(Integer, primary_key=True)
    Name = Column(String(50), nullable=False)
    Industry = Column(String(25), nullable=False)
    CountryofHeadquarters = Column(String(50), nullable=False)
    Type = Column(String(25), nullable=False)

class PersonCompany(Base):
    __tablename__ = 'person_company'
    PersonID = Column(Integer, ForeignKey('person.PersonID'), primary_key=True)
    CompanyID = Column(Integer, ForeignKey('company.CompanyID'), primary_key=True)
    Role = Column(String(25), nullable=False)
    