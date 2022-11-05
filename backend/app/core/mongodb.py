import logging
from motor.motor_asyncio import AsyncIOMotorClient
from beanie import init_beanie

from app.api.users.models import User
from app.api.messages.models import Message
from app.api.rooms.models import Room
from app.config.settings import common_settings


async def init_db():
    client = AsyncIOMotorClient(common_settings.MONGODB_URL)
    db = client[common_settings.MONGODB_DB_NAME]
    await init_beanie(database=db, document_models=[User, Message, Room])
