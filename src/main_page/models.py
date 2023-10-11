from ..database import Base

from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from sqlalchemy import TIMESTAMP, Integer, Boolean, ForeignKey, JSON, String, Text
from sqlalchemy.dialects.postgresql import ARRAY



class Main_page(Base):
    __tablename__ = "main_pages"

    id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str] = mapped_column(nullable=False)
    subtitle: Mapped[str] = mapped_column(nullable=False)
    history_block: Mapped[str] = mapped_column(nullable=False)
    main_image: Mapped[str] = mapped_column(unique=True, nullable=False)
    carousel_image: Mapped[list[str]] = mapped_column(ARRAY(Text), nullable=False)
