from backend.api.searchAPI.pydantic_models import NewsArticle, AnalyticsResult, IdentityScores, Risks
from backend.api.searchAPI.summary import get_analytics_summary
from typing import List


def get_analytics(newsArticles: List[NewsArticle]) -> AnalyticsResult:
    risk_dict = {}
    categories_dict = {}
    identity_dict = {"identity_0_19": int, "identity_20_39": int, "identity_40_59": int, "identity_60_79": int, "identity_80_100": int}
    summary_articles = []
    
    for newsArticle in newsArticles:
        # calculations for risk, categories
        risk = newsArticle.risk_rating.lower()
        category = newsArticle.category
        identity = newsArticle.score

        add_to_dict(risk_dict, risk)
        add_to_dict(categories_dict, category)
        add_to_dict(identity_dict, get_identity_group(identity))
        print("3333")
        # summary
        if (identity > 75):
            summary_articles.append(newsArticle.summary)

        analytics_summary = get_analytics_summary(summary_articles)
        print("4444")
        return AnalyticsResult(
            risks=Risks(**risk_dict),
            categories= categories_dict,
            identityScores=IdentityScores(**identity_dict),
            summary=analytics_summary,
        )


def add_to_dict(count_dict:dict, key:str) -> None:
    if(key in count_dict):
        count_dict[key] += 1
    else:
        count_dict[key] = 1


def get_identity_group(identityScore: int) -> str:
    score_category = identityScore // 20
    match score_category:
        case 0:
            return "identity_0_19"
        case 1:
            return "identity_20_39"
        case 2:
            return "identity_40_59"
        case 3:
            return "identity_60_79"
        case _:
            return "identity_80_100"
