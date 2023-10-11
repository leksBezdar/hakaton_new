import re

from pydantic import BaseModel, Field, validator
from typing import Dict, Optional

from .config import (
    MIN_USERNAME_LENGTH as user_min_len,
    MAX_USERNAME_LENGTH as user_max_len,
    MIN_PASSWORD_LENGTH as pass_min_len,
    MAX_PASSWORD_LENGTH as pass_max_len,
                    )

class UserBase(BaseModel):
    username: Optional[str]
    is_active: bool = Field(False)
    is_superuser: bool = Field(False)
    

class UserCreate(UserBase):
    username: str
    password: str
    
        
    @validator("username")
    def validate_username_length(cls, value):
        if len(value) < int(user_min_len) or len(value) > int(user_max_len):
            raise ValueError("Username must be between 5 and 15 characters")
        
        return value
    
    @validator("password")
    def validate_password_complexity(cls, value):
        if len(value) < int(pass_min_len) or len(value) > int(pass_max_len):
            raise ValueError("Password must be between 8 and 30 characters")
        
        if not re.search(r"\d", value):
            raise ValueError("Password must contain at least one digit")
        
        if not re.search(r"[A-Z]", value):
            raise ValueError("Password must contain at least one uppercase letter")
        
        if not re.search(r"[!@#$%^&*(),.?\":{}|<>_-]", value):
            raise ValueError("Password must contain at least one special character")
        
        return value
    
class UserUpdate(UserBase):
    password: Optional[str] = None
        

class User(UserBase):
    id: str
    username: str
    is_active: bool
    is_superuser: bool
    
    class Config:
        from_attributes = True
    
class UserCreateDB(UserBase):
    id: str
    hashed_password: Optional[str] = None
      
    
    
class RefreshTokenCreate(BaseModel):
    refresh_token: str
    expires_at: int
    user_id: str

class RefreshTokenUpdate(RefreshTokenCreate):
    user_id: Optional[str] = Field(None)
    
class Token(BaseModel):
    access_token: str
    refresh_token: str
    token_type: str
