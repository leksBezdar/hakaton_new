import uuid

from typing import Optional
from uuid import uuid4

from datetime import datetime, timedelta, timezone

from fastapi import Request
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import or_, update

from ..auth.models import User 

from ..auth.config import(
    TOKEN_SECRET_KEY,
    ALGORITHM,
    ACCESS_TOKEN_EXPIRE_MINUTES,
    REFRESH_TOKEN_EXPIRE_DAYS
    )
from .dao import RefreshTokenDAO, UserDAO
from ..api.models import Product, Service


