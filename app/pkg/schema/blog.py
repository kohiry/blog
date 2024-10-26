from datetime import datetime
from pydantic import BaseModel

__all__ = [
    "BlogSchema",
    "CreateBlogSchema",
    "UpdateBlogSchema",
    "BaseBlogSchema",
    "GetBlogByIDSchema",
    "DeleteBlogByIDSchema",
]


# Base schema for shared properties, if any are added in the future
class BaseBlogSchema(BaseModel):
    pass


class GetBlogByIDSchema(BaseBlogSchema):
    id: int  # Assuming `id` is an integer in the model


class CreateBlogSchema(GetBlogByIDSchema):
    title: str
    content: str


class UpdateBlogSchema(GetBlogByIDSchema):
    title: str
    content: str


class DeleteBlogByIDSchema(GetBlogByIDSchema):
    pass


class BlogSchema(GetBlogByIDSchema):
    title: str
    content: str
    created_at: datetime
    updated_at: datetime
