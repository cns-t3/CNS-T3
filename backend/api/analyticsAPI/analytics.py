from backend.api.analyticsAPI.pydantic_models import NewsArticle, AnalyticsResult, IdentityScores, Risks
from backend.api.analyticsAPI.summary import get_analytics_summary
from typing import List
import logging

logging.basicConfig(level=logging.INFO)

def get_analytics(newsArticles: List[NewsArticle]) -> AnalyticsResult:
    
    risk_dict = {"low": 0, "medium": 0, "high": 0}
    categories_dict = {}
    identity_dict = {"identity_0_19": 0, "identity_20_39": 0, "identity_40_59": 0, "identity_60_79": 0, "identity_80_100": 0}
    summary_articles = []
    logging.info("1111")
    if len(newsArticles) == 0:
        return AnalyticsResult(
            risks=Risks(**risk_dict),
            categories=categories_dict,  
            identityScores=IdentityScores(**identity_dict),
            summary="",
        )

    for newsArticle in newsArticles:
        logging.info("222222")
        # calculations for risk, categories
        risk = newsArticle.risk_rating.lower()
        category = newsArticle.category
        identity = newsArticle.score

        add_to_dict(risk_dict, risk)
        add_to_dict(categories_dict, category)
        add_to_dict(identity_dict, get_identity_group(identity))
        logging.info("33333333")
        # summary
        if identity > 75:
            summary_articles.append(newsArticle.summary)
    logging.info("444444444")
    analytics_summary = get_analytics_summary(summary_articles)

    # convert risks count to percentage
    risk_dict = get_risk_percentage(risk_dict)
    logging.info("55555555555")
    return AnalyticsResult(
        risks=Risks(**risk_dict),
        categories=categories_dict,  
        identityScores=IdentityScores(**identity_dict),
        summary=analytics_summary,
    )


def add_to_dict(count_dict: dict, key: str) -> None:
    if key != "" or key != None:
        if key in count_dict:
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


def get_risk_percentage(risk_dict: dict) -> dict:
    total = risk_dict["low"] + risk_dict["medium"] + risk_dict["high"]
    risk_dict["low"] = round(risk_dict["low"] / total * 100, 1)
    risk_dict["medium"] = round(risk_dict["medium"] / total * 100, 1)
    risk_dict["high"] = round(risk_dict["high"] / total * 100, 1)
    return risk_dict
