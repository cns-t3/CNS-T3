from fastapi import FastAPI, HTTPException, Query, Depends
from sqlalchemy.orm import Session
from pydantic_models import PersonSchema
from database import get_db
from person_service import search_person_by_name

app = FastAPI()


@app.get("/persons/search/")
async def search_persons_by_name(
    name: str = Query(None, min_length=1), db: Session = Depends(get_db)
):
    if not name:
        raise HTTPException(status_code=400, detail="Name parameter is required")

    person, company_name = search_person_by_name(db, name)

    if not person:
        raise HTTPException(
            status_code=404, detail="No persons found with the provided name"
        )

    # convert ORM to Pydantic model
    return PersonSchema(
        person_id=person.PersonID,
        name=person.Name,
        occupation=person.Occupation,
        dob=person.DoB.strftime("%Y-%m-%d") if person.DoB else None,
        nationality=person.Nationality,
        description=person.Description,
        company=company_name,
        country_of_residency=person.CountryOfResidency,
        pep_status=person.PEPStatus,
        source_of_wealth=person.SourceOfWealth,
        img_url=person.ImgURL,
    )
