from typing import Optional

from fastapi import Request
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import or_, update

from ..auth.models import User 

from .dao import ProblemDAO
from .models import Problem

from . import schemas


class ProblemCRUD:
    
    def __init__(self, db: AsyncSession):
        self.db = db
        
    async def create_problem(self, problem: schemas.ProblemCreate) -> Problem:
        
        db_problem = await ProblemDAO.add(
            self.db,
            schemas.ProblemCreate(
            **problem.model_dump(),
            )
        )

        self.db.add(db_problem)
        await self.db.commit()
        await self.db.refresh(db_problem)
        
        
        return db_problem
        

    async def get_problem(self, problem_title: str = None, problem_id: int = None) -> Optional[Problem]:
        
        problem = await ProblemDAO.find_one_or_none(self.db, or_(
            Problem.title == problem_title,
            Problem.id == problem_id))
        
        return problem
    
    
    async def get_all_problems(self, *filter, offset: int = 0, limit: int = 100, **filter_by) -> list[Problem]:
        
        problems = await ProblemDAO.find_all(self.db, *filter, offset=offset, limit=limit, **filter_by)
        
        return problems or {"message": "no problems found"}
    
    
    async def update_problem(self, problem_id: int, problem_in: schemas.ProblemUpdate):
        
        obj_in = schemas.ProblemUpdate(**problem_in.model_dump())
        
        problem_update = await ProblemDAO.update(
                self.db,
                Problem.id == problem_id,
                obj_in=obj_in)
        
        await self.db.commit()
        
        return problem_update
    
    
    async def delete_problem(self, problem_title: str = None, problem_id: int = None) -> None:
        
        await ProblemDAO.delete(self.db, or_(
            problem_id == Problem.id,
            problem_title == Problem.title))
        
        await self.db.commit()


class DatabaseManager:
    def __init__(self, db: AsyncSession):
        self.db = db
        self.problem_crud = ProblemCRUD(db)

    # Применение изменений к базе данных
    async def commit(self):
        await self.db.commit()