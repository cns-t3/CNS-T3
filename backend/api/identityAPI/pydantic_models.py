from pydantic import BaseModel
from typing import List
from typing import Union


class NewsArticle(BaseModel):
    news_id: int
    title: str
    content: str
    publisher: str
    publishedAt: str
    image_url: str
    source_url: str
    risk_rating: str
    summary: str
    score: int
    category: str
    subject_summary: str


class Person(BaseModel):
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


class SearchResult(BaseModel):
    person: Person
    newsArticles: List[NewsArticle]