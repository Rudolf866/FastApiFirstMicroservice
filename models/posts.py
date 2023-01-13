from datetime import datetime

from pydantic import BaseModel


class PostsBase(BaseModel):
    id: int
    title: str
    text: str
    date: datetime

    class Config:
        orm_mode = True


class PostCreate(BaseModel):
    title: str
    text: str
    date: datetime

    class Config:
        orm_mode = True


class PostUpdate(BaseModel):
    title: str
    text: str
    date: datetime

    class Config:
        orm_mode = True
