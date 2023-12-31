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
    is_superuser: bool = Field(False)
    

class UserCreate(UserBase):
    username: str
    password: str
    
        
    @validator("username")
    def validate_username_length(cls, value):
        if len(value) < int(user_min_len) or len(value) > int(user_max_len):
            raise ValueError("Username must be between 1 and 15 characters")
        
        return value
    
    @validator("password")
    def validate_password_complexity(cls, value):
        if len(value) < int(pass_min_len) or len(value) > int(pass_max_len):
            raise ValueError("Password must be between 3 and 30 characters")
        
        return value
    
class UserUpdate(UserBase):
    password: Optional[str] = None


class UserLogin(BaseModel):
    username: str
    password:str
        

class User(UserBase):
    id: str
    username: str
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
