from pydantic import BaseSettings
from functools import lru_cache


class Settings(BaseSettings):
    APP_NAME: str = "AI Recruitment Service"
    APP_VERSION: str = "1.0.0"

    ELASTICSEARCH_HOST: str = "http://localhost:9200"
    CANDIDATE_INDEX: str = "candidates"
    JOB_INDEX: str = "jobs"

    class Config:
        #env_file = ".env"  
        case_sensitive = True


@lru_cache()
def get_settings() -> Settings:
    return Settings()

