from sqlalchemy.orm import Session
from backend.api.personAPI.sqlalchemy_models import Person, Company, PersonCompany


def search_person_by_name(db: Session, name: str):
    # Search database for persons with search query
    persons = db.query(Person).filter(Person.Name.ilike(f"%{name}%")).all()
    if not persons:
        return None, None

    # Get company information
    person = persons[0]
    companies = (
        db.query(Company)
        .join(PersonCompany, Company.CompanyID == PersonCompany.CompanyID)
        .filter(PersonCompany.PersonID == person.PersonID)
        .all()
    )
    company_name = companies[0].Name if companies else None

    return person, company_name
