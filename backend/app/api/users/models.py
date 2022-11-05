from datetime import datetime
from typing import Optional

from beanie import Document, Indexed
from pydantic import Field, EmailStr, BaseModel


class Profile(BaseModel):
    username: Indexed(str)
    photo: Optional[str] = None
    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: datetime = Field(default_factory=datetime.utcnow)


class User(Document):
    class DocumentMeta:
        collection_name = "users"

    email: EmailStr
    is_superuser: bool = False
    active: bool = True
    verified: bool = False
    hashed_password: str
    username: Optional[Indexed(str)] = None
    photo: Optional[str] = None
    verification_code: str
    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: datetime = Field(default_factory=datetime.utcnow)
