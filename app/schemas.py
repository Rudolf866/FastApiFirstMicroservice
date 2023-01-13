from pydantic import BaseModel
from typing import Optional
from datetime import datetime


class PostBase(BaseModel):
    title: str = ''
    text: str = ''
    date: datetime

    class Config:
        orm_mode = True


class PostList(PostBase):
    pass



class PostCreate(PostBase):
    pass
