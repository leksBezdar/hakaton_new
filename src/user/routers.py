from typing import Optional
from fastapi import APIRouter, Depends, Request

from ..auth.service import DatabaseManager
from ..auth.dependencies import get_current_active_user, get_current_user
from ..auth.models import User
from sqlalchemy.ext.asyncio import AsyncSession
from ..database import get_async_session
from ..auth.schemas import User

from .dao import *


router = APIRouter()


@router.post("/get_user_by_token/", response_model=User)
async def get_user_by_token(
    request: Request,
    access_token: str, 
    db: AsyncSession = Depends(get_async_session),
) -> Optional[User]:
    
    db_manager = DatabaseManager(db)
    token_crud = db_manager.token_crud
    user_crud = db_manager.user_crud
    
    user_id = token_crud.get_access_token_payload(access_token=access_token)
    
    return user_crud.get_existing_user(user_id=user_id)



    



