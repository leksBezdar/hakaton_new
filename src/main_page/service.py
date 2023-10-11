from typing import Optional

from fastapi import Request
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import or_, update

from ..auth.models import User 

from .dao import Main_pageDAO
from .models import Main_page

from . import schemas


class Main_pageCRUD:
    
    def __init__(self, db: AsyncSession):
        self.db = db
        
    async def create_main_page(self, main_page: schemas.Main_pageCreate) -> Main_page:
        
        db_main_page = await Main_pageDAO.add(
            self.db,
            schemas.Main_pageCreate(
            **main_page.model_dump(),
            )
        )

        self.db.add(db_main_page)
        await self.db.commit()
        await self.db.refresh(db_main_page)
        
        
        return db_main_page
        

    async def get_main_page(self, main_page_title: str = None, main_page_id: int = None) -> Optional[Main_page]:
        
        main_page = await Main_pageDAO.find_one_or_none(self.db, or_(
            Main_page.title == main_page_title,
            Main_page.id == main_page_id))
        
        return main_page
    
    
    async def get_all_main_pages(self, *filter, offset: int = 0, limit: int = 100, **filter_by) -> list[Main_page]:
        
        main_pages = await Main_pageDAO.find_all(self.db, *filter, offset=offset, limit=limit, **filter_by)
        
        return main_pages or {"message": "no main_pages found"}
    
    
    async def update_main_page(self, main_page_id: int, main_page_in: schemas.Main_pageUpdate):
        
        obj_in = schemas.Main_pageUpdate(**main_page_in.model_dump())
        
        main_page_update = await Main_pageDAO.update(
                self.db,
                Main_page.id == main_page_id,
                obj_in=obj_in)
        
        await self.db.commit()
        
        return main_page_update
    
    
    async def delete_main_page(self, main_page_title: str = None, main_page_id: int = None) -> None:
        
        await Main_pageDAO.delete(self.db, or_(
            main_page_id == Main_page.id,
            main_page_title == Main_page.title))
        
        await self.db.commit()


class DatabaseManager:
    def __init__(self, db: AsyncSession):
        self.db = db
        self.main_page_crud = Main_pageCRUD(db)

    # Применение изменений к базе данных
    async def commit(self):
        await self.db.commit()