from datetime import datetime

from typing import Optional, List
from beanie import Document, Indexed
from pydantic import Field

from app.api.users.schemas import UserSchema
from app.api.messages.schemas import MessageSchema


class Room(Document):
    class DocumentMeta:
        collection_name = "rooms"

    room_name: Indexed(str)
    members: List[UserSchema] = []
    messages: List[MessageSchema] = []
    date_created: datetime = Field(default_factory=datetime.utcnow)
    last_pinged: datetime = Field(default_factory=datetime.utcnow)
    active: bool = False
