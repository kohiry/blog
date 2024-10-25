from app.pkg.common import BaseSchema

__all__ = [
    "BlogSchema",
    "GetBlogByNameSchema",
    "CreateBlogSchema",
    "UpdateBlogSchema",
    "DeleteBlogByNameSchema",
    "BaseBlogSchema",
]


class BaseBlogSchema(BaseSchema):
    pass


class GetBlogByNameSchema(BaseBlogSchema):
    name: str


class CreateBlogSchema(BaseBlogSchema):
    name: str
    author: str


class UpdateBlogSchema(BaseBlogSchema):
    old_name: str
    name: str
    author: str


class DeleteBlogByNameSchema(BaseBlogSchema):
    name: str


class BlogSchema(BaseBlogSchema):
    name: str
    author: str
