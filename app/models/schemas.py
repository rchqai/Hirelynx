from pydantic import BaseModel, HttpUrl, EmailStr
from typing import List, Optional

class skill(BaseModel):
    name: str
    level: Optional[str] = None

class CandidateSearchRequest(BaseModel):
    
    query: str
    skills: List[str] = []
    experience_min: Optional[float] = None
    experience_max: Optional[float] = None
    location: Optional[str] = None
    limit: int = 20
    offset: int = 0


class CandidateSummary(BaseModel):
    
    candidate_id: str
    name: Optional[str] = None
    title: Optional[str] = None 
    skills: List[str] = []
    experience_years: Optional[float] = None
    location: Optional[str] = None
    score: float


class CandidateSearchResponse(BaseModel):
    results: List[CandidateSummary]
    total: int

class CandidateSearchRequest(BaseModel):
    
    query: str
    skills: List[str] = []
    experience_min: Optional[float] = None
    experience_max: Optional[float] = None
    location: Optional[str] = None
    limit: int = 20
    offset: int = 0


class CandidateSummary(BaseModel):
    
    candidate_id: str
    name: Optional[str] = None
    title: Optional[str] = None  
    skills: List[str] = []
    experience_years: Optional[float] = None
    location: Optional[str] = None
    score: float


class CandidateSearchResponse(BaseModel):
    results: List[CandidateSummary]
    total: int

class CandidateSearchRequest(BaseModel):
    
    query: str
    skills: List[str] = []
    experience_min: Optional[float] = None
    experience_max: Optional[float] = None
    location: Optional[str] = None
    limit: int = 20
    offset: int = 0


class CandidateSummary(BaseModel):
    
    candidate_id: str
    name: Optional[str] = None
    title: Optional[str] = None  
    skills: List[str] = []
    experience_years: Optional[float] = None
    location: Optional[str] = None
    score: float


class JobRecommendationResponse(BaseModel):
    jobs: List[JobSummary]
