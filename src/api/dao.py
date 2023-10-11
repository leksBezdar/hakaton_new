from .models import Service, Product, Address
from .schemas import ServiceCreateDB, ServiceUpdate, ProductCreateDB, ProductUpdate, AddressCreateDB, AddressUpdate

from ..dao import BaseDAO


    
class ProductDAO(BaseDAO[Product, ProductCreateDB, ProductUpdate]):
    model = Product
    
    
class ServiceDAO(BaseDAO[Service, ServiceCreateDB, ServiceUpdate]):
    model = Service


class AddressDAO(BaseDAO[Service, AddressCreateDB, AddressUpdate]):
    model = Address