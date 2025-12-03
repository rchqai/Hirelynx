from fastapi import APIRouter, Depends
from app.models.schemas import CandidateSearchRequest, CandidateSearchResponse
from app.services.candidate_search_service import CandidateSearchService

router = APIRouter()

def get_candidate_search_service():
    return CandidateSearchService()

@router.post("/candidates", response_model=CandidateSearchResponse)
async def candidate_search(
    payload: CandidateSearchRequest,
    service: CandidateSearchService = Depends(get_candidate_search_service)
):
    results = await service.search_candidates(payload)
    return CandidateSearchResponse(results=results)