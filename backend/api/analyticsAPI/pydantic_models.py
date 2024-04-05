from pydantic import BaseModel
from typing import List


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
    newsArticle: List[NewsArticle]
    

class Risks(BaseModel):
    low: float
    medium: float
    high: float


class IdentityScores(BaseModel):
    identity_0_20: int
    identity_21_40: int
    identity_41_60: int
    identity_61_80: int
    identity_81_100: int


class AnalyticsResult(BaseModel):
    risks: Risks
    categories: dict
    identityScores: IdentityScores
    summary: str