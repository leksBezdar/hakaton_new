from .models import Service, Product
from .schemas import ServiceCreateDB, ServiceUpdate, ProductCreateDB, ProductUpdate

from ..dao import BaseDAO


    
class ProductDAO(BaseDAO[Product, ProductCreateDB, ProductUpdate]):
    model = Product
    
    
class ServiceDAO(BaseDAO[Service, ServiceCreateDB, ServiceUpdate]):
    model = Service