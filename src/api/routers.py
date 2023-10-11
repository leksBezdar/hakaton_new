from fastapi import APIRouter, Depends, Request, Response
from fastapi.responses import JSONResponse

from sqlalchemy.ext.asyncio import AsyncSession

from typing import Optional

from src.auth.models import User

from . import schemas

from ..auth.dependencies import get_current_active_user, get_current_superuser
from .models import Product, Service
from .service import DatabaseManager
from ..database import get_async_session


router = APIRouter()


@router.post("/create_product/", response_model=schemas.Product)
async def create_product(
    product_data: schemas.ProductCreate,
    db: AsyncSession = Depends(get_async_session),
) -> Product:
    db_manager = DatabaseManager(db)
    product_crud = db_manager.product_crud
    
    return await product_crud.create_product(product=product_data)


@router.get("/get_product/", response_model=schemas.Product)
async def get_product(
    product_name: str = None,
    product_id: int = None,
    db: AsyncSession = Depends(get_async_session),
) -> Product:
    db_manager = DatabaseManager(db)
    product_crud = db_manager.product_crud
    
    return await product_crud.get_product(product_name=product_name, product_id=product_id)


@router.get("/read_all_products")
async def get_all_products(
    offset: int = 0,
    limit: int = 10,
    db: AsyncSession = Depends(get_async_session),
):
    db_manager = DatabaseManager(db)
    product_crud = db_manager.product_crud
    
    return await product_crud.get_all_products(offset=offset, limit=limit)


@router.put("/update_product", response_model=schemas.Product)
async def update_product(
    product_id: int,
    product_data: schemas.ProductUpdate,
    db: AsyncSession = Depends(get_async_session),
):
    
    db_manager = DatabaseManager(db)
    product_crud = db_manager.product_crud
    
    return await product_crud.update_product(product_id=product_id, product_in=product_data)


@router.delete("/delete_product")
async def delete_product(
    product_name: str = None,
    product_id: int = None,
    db: AsyncSession = Depends(get_async_session),
    super_user: User = Depends(get_current_superuser)
):
    
    db_manager = DatabaseManager(db)
    product_crud = db_manager.product_crud
    
    await product_crud.delete_product(product_name=product_name, product_id=product_id)
    
    response = JSONResponse(content={
        "message": "Delete successful",
    })
    
    return response


@router.post("/create_service/", response_model=schemas.Service)
async def create_service(
    service_data: schemas.ServiceCreate,
    db: AsyncSession = Depends(get_async_session),
) -> Service:
    db_manager = DatabaseManager(db)
    service_crud = db_manager.service_crud
    
    return await service_crud.create_service(service=service_data)


@router.get("/get_service/", response_model=schemas.Service)
async def get_service(
    service_name: str = None,
    service_id: int = None,
    db: AsyncSession = Depends(get_async_session),
) -> Service:
    db_manager = DatabaseManager(db)
    service_crud = db_manager.service_crud
    
    return await service_crud.get_service(service_name=service_name, service_id=service_id)


@router.get("/read_all_services")
async def get_all_services(
    offset: int = 0,
    limit: int = 10,
    db: AsyncSession = Depends(get_async_session),
):
    db_manager = DatabaseManager(db)
    service_crud = db_manager.service_crud
    
    return await service_crud.get_all_services(offset=offset, limit=limit)


@router.put("/update_service", response_model=schemas.Service)
async def update_service(
    service_id: int,
    service_data: schemas.ServiceUpdate,
    db: AsyncSession = Depends(get_async_session),
):
    
    db_manager = DatabaseManager(db)
    service_crud = db_manager.service_crud
    
    return await service_crud.update_service(service_id=service_id, service_in=service_data)


@router.delete("/delete_service")
async def delete_service(
    service_name: str = None,
    service_id: int = None,
    db: AsyncSession = Depends(get_async_session),
    super_user: User = Depends(get_current_superuser)
):
    
    db_manager = DatabaseManager(db)
    service_crud = db_manager.service_crud
    
    await service_crud.delete_service(service_name=service_name, service_id=service_id)
    
    response = JSONResponse(content={
        "message": "Delete successful",
    })
    
    return response