from typing import Union

from app.api.auth.utils import verify_hashed_data
from app.api.users.utils import get_user_by_email
from app.api.users.models import User


async def verification_user(user_email: str, verification_code: str):
    """Verify user email code."""
    user = await get_user_by_email(user_email)
    if not user or not verify_hashed_data(verification_code, user.verification_code):
        return False
    return user


async def authenticate_user(user_email: str, password: str) -> Union[User, bool]:
    """Authenticate user by password."""
    user = await get_user_by_email(user_email)
    if not user or not verify_hashed_data(password, user.hashed_password):
        return False
    return user
