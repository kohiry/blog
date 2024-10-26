from datetime import datetime
from pydantic import BaseModel

__all__ = [
    "PostsSchema",
    "CreatePostsSchema",
    "UpdatePostsSchema",
    "BasePostsSchema",
    "GetPostsByIDSchema",
    "DeletePostsByIDSchema",
]


# Base schema for shared properties, if any are added in the future
class BasePostsSchema(BaseModel):
    pass


class GetPostsByIDSchema(BasePostsSchema):
    id: int  # Assuming `id` is an integer in the model


class CreatePostsSchema(GetPostsByIDSchema):
    title: str
    content: str


class UpdatePostsSchema(GetPostsByIDSchema):
    title: str
    content: str


class DeletePostsByIDSchema(GetPostsByIDSchema):
    pass


class PostsSchema(GetPostsByIDSchema):
    title: str
    content: str
    created_at: datetime
    updated_at: datetime
