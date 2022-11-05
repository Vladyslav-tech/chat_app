from typing import Optional
from pydantic import EmailStr, BaseModel, Field


class UserBaseSchema(BaseModel):
    username: Optional[str] = None
    email: EmailStr


class UserSchema(BaseModel):
    id: str = Field(alias="_id")
    username: str
    photo: Optional[str] = None
