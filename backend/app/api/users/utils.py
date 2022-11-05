from .models import User


async def get_user_by_email(email: str):
    return await User.find_one(User.email == email)
