from pydantic import BaseModel, EmailStr, Field, validator
from typing import Dict, List, Optional


class Main_page(BaseModel):
    title: str
    subtitle: str
    supertitle: str
    history_block: str
    main_image: str
    carousel_image: List

class Main_pageCreateDB(Main_page):
    id: int


class Main_pageCreate(Main_page):
    pass


class Main_pageUpdate(Main_page):
    title: Optional[str] = None
    subtitle: Optional[str] = None
    supertitle: Optional[str] = None
    history_block: Optional[str] = None
    main_image: Optional[str] = None
    carousel_image: Optional[List] = None