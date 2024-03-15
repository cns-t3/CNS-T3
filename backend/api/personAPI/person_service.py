from sqlalchemy.orm import Session
from backend.api.personAPI.sqlalchemy_models import Person, Company, PersonCompany
from backend.api.personAPI.pydantic_models import PersonSchema


def search_person_by_name(db: Session, name: str):
    # Search database for persons with search query
    persons = db.query(Person).filter(Person.Name.ilike(f"%{name}%")).all()
    if not persons:
        return None, None, None

    # Get company information
    person = persons[0]
    companies = (
        db.query(Company)
        .join(PersonCompany, Company.CompanyID == PersonCompany.CompanyID)
        .filter(PersonCompany.PersonID == person.PersonID)
        .all()
    )
    person_companies = (
        db.query(PersonCompany).filter(PersonCompany.PersonID == person.PersonID).all()
    )

    company_name = companies[0].Name if companies else None
    role_name = person_companies[0].Role if person_companies else None

    return person, company_name, role_name


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
