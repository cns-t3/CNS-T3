from pydantic import BaseModel

class NewsArticle(BaseModel):
    news_id: int
    title: str
    content: str
    publisher: str
    publishedAt: str
    image_url: str = ""
    source_url: str
    risk_rating: str
    risk_justification: str
    summary: str
    score: int
    category: str
    subject_summary: str