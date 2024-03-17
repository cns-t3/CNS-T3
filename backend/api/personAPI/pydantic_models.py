from pydantic import BaseModel

class PersonSchema(BaseModel):
    person_id: int
    name: str
    occupation: str
    dob: str
    nationality: str
    description: str
    company: str
    country_of_residency: str
    pep_status: bool
    source_of_wealth: str
    img_url: str
