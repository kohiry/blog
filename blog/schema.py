from pydantic import BaseModel, EmailStr
from datetime import datetime
from uuid import UUID
from typing import List

# how fucking doing that shit


class UserSchema(BaseModel):
    username: str
    email: EmailStr
    id: UUID


class PostSchema(BaseModel):
    id: UUID
    author: UserSchema
    title: str
    description: str
    created: datetime
    updated: datetime


class PostLikesSchema(BaseModel):
    post: PostSchema
    who_likes: List[UserSchema]


class CommentSchema(BaseModel):
    user_id: UserSchema
    post_id: PostSchema
    description: str
    created: datetime
    updated: datetime
