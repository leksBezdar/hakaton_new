from .models import Main_page
from .schemas import Main_pageCreateDB, Main_pageUpdate 

from ..dao import BaseDAO


    
class Main_pageDAO(BaseDAO[Main_page, Main_pageCreateDB, Main_pageUpdate]):
    model = Main_page