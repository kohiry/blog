from sqlalchemy import Column, Integer, String
from app.pkg.models import BaseModel
from app.pkg.models.mixins import TimestampMixin


__all__ = [
    "BlogMessage",
]


class BlogMessage(TimestampMixin, BaseModel):
    __tablename__ = "blog_message"

    id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String, nullable=False)
    content = Column(String, nullable=False)

    def __repr__(self):
        return (
            f"<BlogMessage(id={self.id}, title='{self.title}',"
            f" created_at={self.created_at}, updated_at={self.updated_at})>"
        )
