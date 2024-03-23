from sqlalchemy.orm import Session
from backend.api.personAPI.sqlalchemy_models import Person, Company, PersonCompany
from backend.api.personAPI.pydantic_models import PersonSchema
import Levenshtein
from typing import List, Tuple, Optional

def get_person_by_id(db: Session, person_id: int) -> Tuple[Person, str, str]:
    
    result = (
        db.query(Person, PersonCompany, Company)
        .filter(
            Person.PersonID.ilike(person_id),
            Person.PersonID == PersonCompany.PersonID,
            PersonCompany.CompanyID == Company.CompanyID,
        )
        .all()
    )
    
    if not result:
        return None, None, None
    
    person = result[0][0]
    company_name = result[0][2].Name
    role_name = result[0][1].Role
    return person, company_name, role_name
    

def search_person_by_name(db: Session, name: str) -> List[Tuple[Person, str, str]]:
    # Search database for persons with search query
    persons = (
        db.query(Person, PersonCompany, Company)
        .filter(
            Person.Name.ilike(f"%{name}%"),
            Person.PersonID == PersonCompany.PersonID,
            PersonCompany.CompanyID == Company.CompanyID,
        )
        .all()
    )
    if len(persons) == 0:
        return []

    results = []

    for person, person_company, company in persons:
        company_name = company.Name
        role_name = person_company.Role
        results.append((person, company_name, role_name))

    return results

def get_all_persons(db: Session):
    persons = (
        db.query(Person, PersonCompany, Company)
        .filter(
            Person.PersonID == PersonCompany.PersonID,
            PersonCompany.CompanyID == Company.CompanyID,
        )
        .all()
    )

    person_return_arr = []
    for person, personCompany, company in persons:
        person_return = PersonSchema(
            person_id=person.PersonID,
            name=person.Name,
            occupation=person.Occupation,
            role=personCompany.Role if personCompany.Role else None,
            dob=person.DoB.strftime("%Y-%m-%d") if person.DoB else None,
            nationality=person.Nationality,
            description=person.Description,
            company=company.Name if company.Name else None,
            country_of_residency=person.CountryOfResidency,
            pep_status=person.PEPStatus,
            source_of_wealth=person.SourceOfWealth,
            img_url=person.ImgURL,
        )
        person_return_arr.append(person_return)
    return person_return_arr


def get_similar_names(db: Session, name: str, similarity_threshold: float = 0.7) -> List[Tuple[Person, str, str]]:

    persons = (
        db.query(Person, PersonCompany, Company)
        .join(PersonCompany, Person.PersonID == PersonCompany.PersonID)
        .join(Company, PersonCompany.CompanyID == Company.CompanyID)
        .all()
    )

    similar_names = []
    for person, person_company, company in persons:
        similarity = Levenshtein.ratio(name.lower(), person.Name.lower())
        if similarity >= similarity_threshold:
            company_name = company.Name
            role_name = person_company.Role
            similar_names.append((person, company_name, role_name))

    return similar_names