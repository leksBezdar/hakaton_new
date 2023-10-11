from fastapi import APIRouter, Depends, Request, Response
from fastapi.responses import JSONResponse

from sqlalchemy.ext.asyncio import AsyncSession

from typing import Optional

from src.auth.models import User

from . import schemas

from ..auth.dependencies import get_current_superuser
from .models import Main_page
from .service import DatabaseManager
from ..auth.service import DatabaseManager as auth_manager
from ..database import get_async_session


router = APIRouter()


@router.post("/create_main_page/", response_model=schemas.Main_page)
async def create_main_page(
    main_page_data: schemas.Main_pageCreate,
    db: AsyncSession = Depends(get_async_session),
) -> Main_page:
    db_manager = DatabaseManager(db)
    main_page_crud = db_manager.main_page_crud
    
    return await main_page_crud.create_main_page(main_page=main_page_data)


@router.get("/get_main_page/", response_model=schemas.Main_page)
async def get_main_page(
    main_page_title: str = None,
    main_page_id: int = None,
    db: AsyncSession = Depends(get_async_session),
) -> Main_page:
    db_manager = DatabaseManager(db)
    main_page_crud = db_manager.main_page_crud
    
    return await main_page_crud.get_main_page(main_page_title=main_page_title, main_page_id=main_page_id)


@router.get("/read_all_main_pages")
async def get_all_main_pages(
    offset: int = 0,
    limit: int = 10,
    db: AsyncSession = Depends(get_async_session),
):
    db_manager = DatabaseManager(db)
    main_page_crud = db_manager.main_page_crud
    
    return await main_page_crud.get_all_main_pages(offset=offset, limit=limit)


@router.put("/update_main_page", response_model=schemas.Main_page)
async def update_main_page(
    main_page_id: int,
    main_page_data: schemas.Main_pageUpdate,
    db: AsyncSession = Depends(get_async_session),
):
    
    db_manager = DatabaseManager(db)
    main_page_crud = db_manager.main_page_crud
    
    return await main_page_crud.update_main_page(main_page_id=main_page_id, main_page_in=main_page_data)


@router.delete("/delete_main_page")
async def delete_main_page(
    token: str,
    main_page_title: str = None,
    main_page_id: int = None,
    db: AsyncSession = Depends(get_async_session)
):
    
    db_manager = DatabaseManager(db)
    main_page_crud = db_manager.main_page_crud

    auth_manager2 = auth_manager(db)
    token_crud = auth_manager2.token_crud

    if token_crud.get_access_token_payload(token):
    
        await main_page_crud.delete_main_page(main_page_title=main_page_title, main_page_id=main_page_id)

        response = JSONResponse(content={
            "message": "Delete successful",
        })

        return response