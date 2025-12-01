from pydantic import BaseModel, HttpUrl, EmailStr
from typing import List, Optional

class skill(BaseModel):
    name: str
    level: Optional[str] = None

class candidatesearchrequest(BaseModel):
    query: str
    skills : List[skill] = []
    experience_min: Optional[float] = None
    experience_max: Optional[float] = None
    location: Optional[str] = None
    limit: int = 10
    offset: int = 0 

class candidatesummary(BaseModel):
    candidate_id: str
    name: Optional[str] = None
    
    
    