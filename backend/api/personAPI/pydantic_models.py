from pydantic import BaseModel

class PersonSchema(BaseModel):
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
