from fastapi import Depends
from fastapi.security import OAuth2PasswordBearer
from jose import JWTError, jwt

from app.config.settings import auth_settings
from app.api.users.utils import get_user_by_email
from .schemas import TokenData
from .exceptions import AuthorizationException


oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/api/auth/login")


async def get_current_user(token: str = Depends(oauth2_scheme)):
    try:
        payload = jwt.decode(
            token, auth_settings.JWT_SECRET_KEY,
            algorithms=[auth_settings.JWT_ALGORITHM]
        )
        email: str = payload.get("sub")
        if email is None:
            raise AuthorizationException
        token_data = TokenData(email=email)
    except JWTError:
        raise AuthorizationException
    user = await get_user_by_email(email=token_data.email)
    if user is None:
        raise AuthorizationException
    return user
