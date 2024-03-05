from fastapi import FastAPI, HTTPException, status
from backend.api.identityAPI.pydantic_models import SearchResult
from backend.api.identityAPI.identity_matching import identity_matching


app = FastAPI()


@app.post(
    "/identity/",
    response_model=SearchResult,
    tags=["identity"],
    summary="Get identity search results",
    description="Returns a person and an array of news articles with identity matching",
)
async def get_identity_search_results(searchResult: SearchResult):
    try:
        scored_search_result = searchResult.model_dump()
        identity_matching(scored_search_result)
        return scored_search_result
    except Exception:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Internal server error",
        )
