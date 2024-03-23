from fastapi import FastAPI, HTTPException, Query, Depends
from sqlalchemy.orm import Session
from backend.api.personAPI.pydantic_models import PersonSchema
from backend.api.personAPI.database import get_db
from backend.api.personAPI.person_service import (
    get_person_by_id,
    search_person_by_name,
    get_all_persons,
    get_similar_names
)
from fastapi.middleware.cors import CORSMiddleware
from typing import List

app = FastAPI()
origins = [
    "http://localhost:3000",
    "http://4.209.224.122:3000",
]
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/persons/id", response_model=PersonSchema)
async def get_persons_by_id(
    person_id: int = Query(None), db: Session = Depends(get_db)
):
    if not person_id:
        raise HTTPException(status_code=400, detail="Person_id parameter is required")

    person, company_name, role_name = get_person_by_id(db, person_id)

    if not person:
        raise HTTPException(status_code=400, detail="Person not found")

    return PersonSchema(
        person_id=person.PersonID,
        name=person.Name,
        occupation=person.Occupation,
        role=role_name,
        dob=person.DoB.strftime("%Y-%m-%d") if person.DoB else None,
        nationality=person.Nationality,
        description=person.Description,
        company=company_name,
        country_of_residency=person.CountryOfResidency,
        pep_status=person.PEPStatus,
        source_of_wealth=person.SourceOfWealth,
        img_url=person.ImgURL,
    )


@app.get("/persons/search", response_model=List[PersonSchema])
async def search_persons_by_name(
    name: str = Query(None, min_length=1), db: Session = Depends(get_db)
):
    if not name:
        raise HTTPException(status_code=400, detail="Name parameter is required")

    persons = search_person_by_name(db, name)

    if not persons:
        return []

    # convert ORM to Pydantic model
    results = []
    for person, company_name, role_name in persons:
        person_schema = PersonSchema(
            person_id=person.PersonID,
            name=person.Name,
            occupation=person.Occupation,
            role=role_name,
            dob=person.DoB.strftime("%Y-%m-%d") if person.DoB else None,
            nationality=person.Nationality,
            description=person.Description,
            company=company_name,
            country_of_residency=person.CountryOfResidency,
            pep_status=person.PEPStatus,
            source_of_wealth=person.SourceOfWealth,
            img_url=person.ImgURL,
        )
        results.append(person_schema)

    return results


@app.get("/persons")
async def get_persons(db: Session = Depends(get_db)):
    return get_all_persons(db)


@app.get("/persons/similar_search", response_model=List[PersonSchema])
async def search_similar_names(
    name: str = Query(None, min_length=1), db: Session = Depends(get_db)
):
    if not name:
        raise HTTPException(status_code=400, detail="Name parameter is required")

    persons = get_similar_names(db, name)

    if len(persons) == 0:
        return []

    # convert ORM to Pydantic model
    results = []
    for person, company_name, role_name in persons:
        person_schema = PersonSchema(
            person_id=person.PersonID,
            name=person.Name,
            occupation=person.Occupation,
            role=role_name,
            dob=person.DoB.strftime("%Y-%m-%d") if person.DoB else None,
            nationality=person.Nationality,
            description=person.Description,
            company=company_name,
            country_of_residency=person.CountryOfResidency,
            pep_status=person.PEPStatus,
            source_of_wealth=person.SourceOfWealth,
            img_url=person.ImgURL,
        )
        results.append(person_schema)

    return results