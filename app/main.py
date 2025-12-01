
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.core.config import get_settings
from app.core.logging import setup_logging
from app.api.v1.endpoints import health  # baad me yaha candidate_search, resume_parser, recommendations bhi add karenge



logger = setup_logging()


settings = get_settings()
app = FastAPI(
    title=settings.APP_NAME,
    version=settings.APP_VERSION,
    docs_url="/docs",
    redoc_url="/redoc",
)


# CORS 
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # PROD me restrict karna
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)



app.include_router(health.router, prefix="/api/v1", tags=["health"])


@app.on_event("startup")
async def on_startup():
    logger.info("Hirelynx AI Service started.")


@app.on_event("shutdown")
async def on_shutdown():
    logger.info("")