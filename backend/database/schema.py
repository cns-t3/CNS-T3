from pydantic import BaseModel
from datetime import date
from typing import Optional

class PersonBase(BaseModel):
    Name: str
    DoB: date
    CountryOfResidency: str
    Nationality: str
    Occupation: str
    PEPStatus: Optional[bool]
    SourceOfWealth: Optional[str]
    

class PersonCreate(PersonBase):
    pass


class PersonUpdate(PersonBase):
    pass


class Person(PersonBase):
    PersonID: int

    class Config:
        orm_mode = True


class CompanyBase(BaseModel):
    Name: str
    Industry: str
    CountryofHeadquarters: str
    Type: str


class CompanyCreate(CompanyBase):
    pass


class CompanyUpdate(CompanyBase):
    pass


class Company(CompanyBase):
    CompanyID: int

    class Config:
        orm_mode = True


class PersonCompanyBase(BaseModel):
    PersonID: int
    CompanyID: int
    Role: str


class PersonCompanyCreate(PersonCompanyBase):
    pass


class PersonCompanyUpdate(PersonCompanyBase):
    pass


class PersonCompany(PersonCompanyBase):
    class Config:
        orm_mode = True
