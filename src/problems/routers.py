from fastapi import APIRouter, Depends, Request, Response
from fastapi.responses import JSONResponse

from sqlalchemy.ext.asyncio import AsyncSession

from typing import Optional

from src.auth.models import User

from . import schemas

from ..auth.dependencies import get_current_superuser
from .models import Problem
from .service import DatabaseManager
from ..database import get_async_session


router = APIRouter()


@router.post("/create_problem/", response_model=schemas.Problem)
async def create_problem(
    problem_data: schemas.ProblemCreate,
    db: AsyncSession = Depends(get_async_session),
    super_user: User = Depends(get_current_superuser)
) -> Problem:
    db_manager = DatabaseManager(db)
    problem_crud = db_manager.problem_crud
    
    return await problem_crud.create_problem(problem=problem_data)


@router.get("/get_problem/", response_model=schemas.Problem)
async def get_problem(
    problem_title: str = None,
    problem_id: int = None,
    db: AsyncSession = Depends(get_async_session),
) -> Problem:
    db_manager = DatabaseManager(db)
    problem_crud = db_manager.problem_crud
    
    return await problem_crud.get_problem(problem_title=problem_title, problem_id=problem_id)


@router.get("/read_all_problems")
async def get_all_problems(
    offset: int = 0,
    limit: int = 10,
    db: AsyncSession = Depends(get_async_session),
):
    db_manager = DatabaseManager(db)
    problem_crud = db_manager.problem_crud
    
    return await problem_crud.get_all_problems(offset=offset, limit=limit)


@router.put("/update_problem", response_model=schemas.Problem)
async def update_problem(
    problem_id: int,
    problem_data: schemas.ProblemUpdate,
    super_user: User = Depends(get_current_superuser),
    db: AsyncSession = Depends(get_async_session),
):
    
    db_manager = DatabaseManager(db)
    problem_crud = db_manager.problem_crud
    
    return await problem_crud.update_problem(problem_id=problem_id, problem_in=problem_data)


@router.delete("/delete_problem")
async def delete_problem(
    problem_title: str = None,
    problem_id: int = None,
    db: AsyncSession = Depends(get_async_session),
    super_user: User = Depends(get_current_superuser)
):
    
    db_manager = DatabaseManager(db)
    problem_crud = db_manager.problem_crud
    
    await problem_crud.delete_problem(problem_title=problem_title, problem_id=problem_id)
    
    response = JSONResponse(content={
        "message": "Delete successful",
    })
    
    return response