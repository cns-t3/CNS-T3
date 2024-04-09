from pydantic import BaseModel
from typing import List, Dict


class NewsArticle(BaseModel):
    news_id: int
    title: str
    content: str
    publisher: str
    publishedAt: str
    image_url: str = ""
    source_url: str
    risk_rating: str
    summary: str
    score: int
    category: str
    subject_summary: str


class AnalyticsRequest(BaseModel):
    newsArticles: List[NewsArticle]


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


class AnalyticsResult(BaseModel):
    risks: Risks
    categories: Dict[str, int]
    identityScores: IdentityScores
    summary: str