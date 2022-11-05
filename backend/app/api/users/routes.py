from typing import List
import logging

from fastapi import APIRouter

from .models import User
from .schemas import UserBaseSchema


logger = logging.getLogger(__name__)
router = APIRouter()


@router.get("/", response_description="Get all users", response_model=List[UserBaseSchema])
async def get_all_user():
    """Get all users"""
    return await User.find_all().to_list()
