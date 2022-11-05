import logging
import random
import string
from datetime import timedelta, datetime
from typing import Optional

from jose import jwt
from passlib.context import CryptContext
from fastapi.security import OAuth2PasswordBearer
from fastapi import BackgroundTasks

from app.config.settings import auth_settings
from app.core.utils import send_email

logger = logging.getLogger(__name__)
pwd_context = CryptContext(schemes=["bcrypt"], default="bcrypt")
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")


def hash_data(data: str) -> str:
    return pwd_context.hash(data)


def verify_hashed_data(data: str, hashed_data: str) -> bool:
    return pwd_context.verify(data, hashed_data)


async def create_token(data: dict, jwt_secret: str, expire_time: int) -> str:
    """Create jwt"""
    to_encode = data.copy()
    expire = datetime.utcnow() + timedelta(minutes=expire_time)

    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, jwt_secret, algorithm=auth_settings.JWT_ALGORITHM)
    return encoded_jwt


async def create_access_token(data: dict):
    """Create access token"""
    return await create_token(
        data=data,
        jwt_secret=auth_settings.JWT_SECRET_KEY,
        expire_time=auth_settings.JWT_ACCESS_TOKEN_EXPIRE,
    )


async def create_refresh_token(data: dict):
    """Create refresh token"""
    return await create_token(
        data=data,
        jwt_secret=auth_settings.JWT_REFRESH_SECRET_KEY,
        expire_time=auth_settings.JWT_REFRESH_TOKEN_EXPIRE,
    )


def create_verification_code(length: int = 6) -> str:
    """Create verification code."""
    return ''.join(random.choice(string.ascii_letters) for _ in range(length))


async def send_verification_code(user_email: str, background_tasks: BackgroundTasks) -> Optional[str]:
    """Send verification code by email."""
    code = create_verification_code()
    message = f"Your verification code: {code}"
    await send_email(background_tasks, [user_email], message)
    return code
