from pydantic import BaseModel
from typing import List


class NewsArticle(BaseModel):
    news_id: int
    title: str
    content: str
    publisher: str
    publishedAt: str
    image_url: str
    source_url: str
    risk_rating: str
    risk_justification: str
    summary: str
    score: int
    category: str
    subject_summary: str


class Person(BaseModel):
    person_id: int | None
    name: str | None
    occupation: str | None
    role: str | None
    dob: str | None
    nationality: str | None
    description: str | None
    company: str | None
    country_of_residency: str | None
    pep_status: str | None
    source_of_wealth: str | None
    img_url: str | None


class SearchResult(BaseModel):
    person: Person
    newsArticles: List[NewsArticle]
