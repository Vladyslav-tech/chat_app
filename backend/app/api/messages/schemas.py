from datetime import datetime
from pydantic import BaseModel, Field


class MessageSchema(BaseModel):
    id: str = Field(alias="_id")
    username: str
    content: str
    created_at: datetime
