import re
from pydantic import BaseModel, EmailStr, Field, validator, Json
from typing import Dict, Optional, Any


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
    phone_number: str
    rented_days: dict


class ServiceCreateDB(Service):
    id: int


class ServiceUpdate(Service):
    name: Optional[str] = None
    price: Optional[str] = None
    description: Optional[str] = None
    time: Optional[str] = None
    img: Optional[str] = None
    type: Optional[str] = None
    phone_number: Optional[str] = None
    rented_days: Optional[dict] = None 


class ServiceCreate(Service):
    pass


class Address(BaseModel):
    address: str

class AddressCreateDB(Address):
    id: int

class AddressCreate(Address):
    pass

class AddressUpdate(Address):
    address: Optional[str] = None

class AddressDelete(Address):
    pass