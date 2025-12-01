from fastapi import APIRouter
from app.core.config import get_settings

router = APIRouter()


@router.get("/health", summary="Health check")
async def health_check():

    settings = get_settings()
    return {
        "status": "ok",
        "service": settings.APP_NAME,
        "version": settings.APP_VERSION,
    }