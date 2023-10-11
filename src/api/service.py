from typing import Optional

from fastapi import Request
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import or_, update

from ..auth.models import User 

from .dao import ProductDAO, ServiceDAO
from .models import Product, Service, Address

from . import schemas


class ProductCRUD:
    
    def __init__(self, db: AsyncSession):
        self.db = db
        
    async def create_product(self, product: schemas.ProductCreate) -> Product:
        
        db_product = await ProductDAO.add(
            self.db,
            schemas.ProductCreate(
            **product.model_dump(),
            )
        )

        self.db.add(db_product)
        await self.db.commit()
        await self.db.refresh(db_product)
        
        
        return db_product
        

    async def get_product(self, product_name: str = None, product_id: int = None) -> Optional[Product]:
        
        product = await ProductDAO.find_one_or_none(self.db, or_(
            Product.name == product_name,
            Product.id == product_id))
        
        return product
    
    
    async def get_all_products(self, *filter, offset: int = 0, limit: int = 100, **filter_by) -> list[Product]:
        
        products = await ProductDAO.find_all(self.db, *filter, offset=offset, limit=limit, **filter_by)
        
        return products or {"message": "no products found"}
    
    
    async def update_product(self, product_id: int, product_in: schemas.ProductUpdate):
        
        obj_in = schemas.ProductUpdate(**product_in.model_dump())
        
        product_update = await ProductDAO.update(
                self.db,
                Product.id == product_id,
                obj_in=obj_in)
        
        await self.db.commit()
        
        return product_update
    
    
    async def delete_product(self, product_name: str = None, product_id: int = None) -> None:
        
        await ProductDAO.delete(self.db, or_(
            product_id == Product.id,
            product_name == Product.name))
        
        await self.db.commit()
        
    
    
class ServiceCRUD:
    
    def __init__(self, db: AsyncSession):
        self.db = db
        
    async def create_service(self, service: schemas.ServiceCreate) -> Service:
        
        db_service = await ServiceDAO.add(
            self.db,
            schemas.ServiceCreate(
            **service.model_dump(),
            )
        )

        self.db.add(db_service)
        await self.db.commit()
        await self.db.refresh(db_service)
        
        
        return db_service
        

    async def get_service(self, service_name: str = None, service_id: int = None) -> Optional[Service]:
        
        service = await ServiceDAO.find_one_or_none(self.db, or_(
            Service.name == service_name,
            Service.id == service_id))
        
        return service
    
    
    async def get_all_services(self, *filter, offset: int = 0, limit: int = 100, **filter_by) -> list[Service]:
        
        services = await ServiceDAO.find_all(self.db, *filter, offset=offset, limit=limit, **filter_by)
        
        return services or {"message": "no services found"}
    
    
    async def update_service(self, service_id: int, service_in: schemas.ServiceUpdate):
        
        obj_in = schemas.ServiceUpdate(**service_in.model_dump())
        
        service_update = await ServiceDAO.update(
                self.db,
                Service.id == service_id,
                obj_in=obj_in)
        
        await self.db.commit()
        
        return service_update
    
    
    async def delete_service(self, service_name: str = None, service_id: int = None) -> None:
        
        await ServiceDAO.delete(self.db, or_(
            service_id == Service.id,
            service_name == Service.name))
        
        await self.db.commit()


class AdressCRUD:

    def __init__(self, db: AsyncSession):
        self.db = db


    async def create_address(self, address: schemas.AddressCreate) -> Address:
        
        db_address = await AddressDAO.add(
            self.db,
            schemas.AddressCreate(
            **address.model_dump(),
            )
        )

        self.db.add(db_address)
        await self.db.commit()
        await self.db.refresh(db_address)
        
        
        return db_address
        

    async def get_address(self, address: str = None, address_id: int = None) -> Optional[Address]:
        
        address = await AddressDAO.find_one_or_none(self.db, or_(
            Address.address == address,
            Address.id == address_id))
        
        return address
    
    
    async def get_all_addresss(self, *filter, offset: int = 0, limit: int = 100, **filter_by) -> list[Address]:
        
        address = await AddressDAO.find_all(self.db, *filter, offset=offset, limit=limit, **filter_by)
        
        return address or {"message": "no address found"}
    
    
    async def update_address(self, address_id: int, address_in: schemas.AddressUpdate):
        
        obj_in = schemas.AddressUpdate(**address_in.model_dump())
        
        address_update = await AddressDAO.update(
                self.db,
                Address.id == address_id,
                obj_in=obj_in)
        
        await self.db.commit()
        
        return address_update
    
    
    async def delete_address(self, address: str = None, address_id: int = None) -> None:
        
        await AddressDAO.delete(self.db, or_(
            address_id == Address.id,
            address == Address.address))
        
        await self.db.commit()
    
# Определение класса для управления всеми crud-классами 
class DatabaseManager:
    def __init__(self, db: AsyncSession):
        self.db = db
        self.product_crud = ProductCRUD(db)
        self.service_crud = ServiceCRUD(db)
        self.address_crud = AdressCRUD(db)

    # Применение изменений к базе данных
    async def commit(self):
        await self.db.commit()
