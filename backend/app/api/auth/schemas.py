from typing import Optional, List
from pydantic import BaseModel, EmailStr, constr, validator


class UserRegistrationSchema(BaseModel):
    email: EmailStr
    username: Optional[str]


class CreateUserSchema(UserRegistrationSchema):
    password: constr(min_length=8)
    password_confirm: str

    @validator('password_confirm')
    def passwords_match(cls, password_confirm, values, **kwargs):
        if 'password' in values and password_confirm != values['password']:
            raise ValueError('passwords do not match')
        return password_confirm


class LoginUserSchema(BaseModel):
    email: EmailStr
    password: constr(min_length=8)


class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    email: Optional[str] = None


class VerifyUserSchema(BaseModel):
    email: EmailStr
    verification_code: str


class EmailSchema(BaseModel):
    email: List[EmailStr]
