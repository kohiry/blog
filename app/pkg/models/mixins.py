from sqlalchemy import DateTime
from datetime import datetime, UTC

from sqlalchemy.orm import mapped_column, Mapped

__all__ = [
    "TimestampMixin",
]


class TimestampMixin:
    created_at: Mapped[datetime] = mapped_column(
        DateTime, default=datetime.now(UTC), nullable=False
    )
    updated_at: Mapped[datetime] = mapped_column(
        DateTime,
        default=datetime.now(UTC),
        onupdate=datetime.now(UTC),
        nullable=False,
    )
