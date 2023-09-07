from pydantic import BaseModel, EmailStr
from datetime import datetime
from uuid import UUID
from typing import List

# how fucking doing that shit


class User(BaseModel):
    username: str
    email: EmailStr
    uuid: UUID


class Post(BaseModel):
    user_id: UUID
    post_id: UUID
    title: str
    description: str
    created: datetime
    updated: datetime
    who_likes: List[UUID]


class Comment(BaseModel):
    user_id: UUID
    post_id: UUID
    description: str
    created: datetime
    updated: datetime
