from sqlalchemy import Integer, String, Index
from sqlalchemy.orm import mapped_column, Mapped

from app.pkg.models.base import BaseORM
from app.pkg.models.mixins import TimestampMixin


__all__ = [
    "PostsModel",
]


class PostsModel(BaseORM, TimestampMixin):
    __tablename__ = "posts"

    __table_args__ = (Index("idx_title_content", "title", "content"),)

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    title: Mapped[str] = mapped_column(String, nullable=False)
    content: Mapped[str] = mapped_column(String, nullable=False)

    def __repr__(self):
        return (
            f"<PostsModel(id={self.id}, title='{self.title}',"
            f" created_at={self.created_at}, updated_at={self.updated_at})>"
        )
