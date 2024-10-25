from abc import ABCMeta, abstractmethod
from sqlalchemy.ext.asyncio import AsyncSession
from app.pkg.common import BaseSchema


__all__ = [
    "BaseRepository",
]


class BaseRepository(metaclass=ABCMeta):
    """Abstract class of pattern repository."""

    @abstractmethod
    def get_by_name(self, query: BaseSchema, session: AsyncSession) -> BaseSchema:
        """Abstract method for getting by name."""
        pass

    @abstractmethod
    def create(self, cmd: BaseSchema, session: AsyncSession) -> BaseSchema:
        """Abstract method for create entity."""
        pass

    @abstractmethod
    def delete_by_name(self, cmd: BaseSchema, session: AsyncSession) -> BaseSchema:
        """Abstract method for delete entity."""
        pass

    @abstractmethod
    def update(self, cmd: BaseSchema, session: AsyncSession) -> BaseSchema:
        """Abstract method for update entity."""
        pass
