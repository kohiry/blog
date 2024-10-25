from sqlalchemy import Column, DateTime
from datetime import datetime, UTC

__all__ = [
    "TimestampMixin",
]


class TimestampMixin:
    created_at = Column(DateTime, default=datetime.now(UTC), nullable=False)
    updated_at = Column(
        DateTime, default=datetime.now(UTC), onupdate=datetime.now(UTC), nullable=False
    )
