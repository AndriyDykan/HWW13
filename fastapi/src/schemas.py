from pydantic import BaseModel,Field,EmailStr
from datetime import date, datetime

class ContactModel(BaseModel):
    name: str
    email: str
    phone_number: str
    birth_date: date
    additional_data: str

class ResponseContact(BaseModel):
    id: int
    name: str
    email: str
    phone_number: str
    birth_date: date
    additional_data: str

    class Config:
        orm_mode = True

class RequestEmail(BaseModel):
    email: EmailStr

class UserModel(BaseModel):
    username: str = Field(min_length=5, max_length=16)
    email: str
    password: str = Field(min_length=6, max_length=10)


class UserDb(BaseModel):
    id: int
    username: str
    email: str
    created_at: datetime
    avatar: str

    class Config:
        orm_mode = True


class UserResponse(BaseModel):
    user: UserDb
    detail: str = "User successfully created"


class TokenModel(BaseModel):
    access_token: str
    refresh_token: str
    token_type: str = "bearer"