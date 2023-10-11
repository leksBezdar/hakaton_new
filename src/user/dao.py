from ..auth.models import User
from ..auth.schemas import UserCreateDB, UserUpdate
from ..dao import BaseDAO

from ..api.models import Service, Product
from ..api.schemas import ServiceCreateDB, ServiceUpdate, ProductCreateDB, ProductUpdate


class UserDAO(BaseDAO[User, UserCreateDB, UserUpdate]):
    model = User
    