from pydantic import BaseModel, EmailStr, Field, validator
from typing import Dict, Optional


class Problem(BaseModel):
    title: str
    description: str
    collected: int
    necessary: int


class ProblemCreateDB(Problem):
    id: int


class ProblemCreate(Problem):
    pass


class ProblemUpdate(Problem):
    title: Optional[str] = None
    description: Optional[str] = None
    collected: Optional[int] = None
    necessary: Optional[int] = None