from typing import Optional, List
from datetime import datetime
from pydantic import BaseModel, Field

from app.api.messages.schemas import MessageSchema
from app.api.users.schemas import UserSchema


class RoomSchema(BaseModel):
    room_name: str
    members: List[UserSchema] = []
    messages: List[MessageSchema] = []
    last_pinged: datetime = Field(default_factory=datetime.utcnow)
    active: bool = False
