from pydantic import BaseModel, EmailStr
from typing import List, Optional

class UserCreate(BaseModel):
    email: EmailStr
    password: str

class User(BaseModel):
    id: int
    email: EmailStr

    class Config:
        orm_mode = True

class Token(BaseModel):
    access_token: str
    token_type: str

class PostCreate(BaseModel):
    text: str

class Post(BaseModel):
    id: int
    text: str
    owner_id: int

    class Config:
        orm_mode = True
