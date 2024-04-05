from fastapi import FastAPI, HTTPException, status
from backend.api.analyticsAPI.pydantic_models import AnalyticsRequest, AnalyticsResult
from backend.api.analyticsAPI.analytics import get_analytics


app = FastAPI()


@app.post(
    "/analytics/",
    response_model=AnalyticsResult,
    tags=["analytics"],
    summary="Get analytics for search results",
    description="Returns a ",
)
async def get_identity_search_results(analyticsRequest: AnalyticsRequest) -> AnalyticsResult:
    try:
        analyticsRequest = get_analytics(analyticsRequest)
        return analyticsRequest
    except Exception:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Internal server error",
        )
