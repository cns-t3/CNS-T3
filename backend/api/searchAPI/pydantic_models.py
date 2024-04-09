from pydantic import BaseModel
from typing import List, Dict, Optional


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
    role: str | None
    dob: str | None
    nationality: str | None
    description: str | None
    company: str | None
    country_of_residency: str | None
    pep_status: str | None
    source_of_wealth: str | None
    img_url: str | None

class Risks(BaseModel):
    low: float
    medium: float
    high: float


class IdentityScores(BaseModel):
    identity_0_19: int
    identity_20_39: int
    identity_40_59: int
    identity_60_79: int
    identity_80_100: int


class Analytics(BaseModel):
    risks: Risks
    categories: Dict[str, int]
    identityScores: IdentityScores
    summary: str


class SearchResult(BaseModel):
    person: Person
    newsArticles: List[NewsArticle]
    analytics: Optional[Analytics] = None
