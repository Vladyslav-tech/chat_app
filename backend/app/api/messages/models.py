from datetime import datetime

from beanie import Document, Indexed
from pydantic import Field


class Message(Document):
    class DocumentMeta:
        collection_name = "messages"

    user_id: Indexed(str)
    room_id: Indexed(str)
    content: str = None
    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: datetime = Field(default_factory=datetime.utcnow)
