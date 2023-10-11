import re

from pydantic import BaseModel, EmailStr, Field, validator
from typing import Dict, Optional


class Product(BaseModel):
    name: str
    price: str
    description: str
    img: str
    type: str


class ProductCreateDB(Product):
    id: int


class ProductCreate(Product):
    pass


class ProductUpdate(Product):
    name: Optional[str] = None
    price: Optional[str] = None
    description: Optional[str] = None
    img: Optional[str] = None
    type: Optional[str] = None 
    


class Service(BaseModel):
    name: str
    price: str
    description: str
    time: str
    img: str
    type: str


class ServiceCreateDB(Service):
    id: int


class ServiceUpdate(Service):
    name: Optional[str] = None
    price: Optional[str] = None
    description: Optional[str] = None
    time: Optional[str] = None
    img: Optional[str] = None
    type: Optional[str] = None


class ServiceCreate(Service):
    pass
