from abc import ABCMeta, abstractmethod
from sqlalchemy.ext.asyncio import AsyncSession
from app.pkg.common import BaseSchema


__all__ = [
    "BaseRepository",
]

from app.pkg.common.model import BaseModel


class BaseRepository(metaclass=ABCMeta):
    """Abstract class of pattern repository."""

    @abstractmethod
    def get_by_id(self, query: BaseSchema, session: AsyncSession) -> BaseSchema:
        """Abstract method for getting by name."""
        pass

    @abstractmethod
    def _check_exist_by_id(
        self,
        query: BaseSchema,
        session: AsyncSession,
    ) -> BaseModel | None:
        pass

    @abstractmethod
    def create(self, cmd: BaseSchema, session: AsyncSession) -> BaseSchema:
        """Abstract method for create entity."""
        pass

    @abstractmethod
    def delete_by_id(self, cmd: BaseSchema, session: AsyncSession) -> BaseSchema:
        """Abstract method for delete entity."""
        pass

    @abstractmethod
    def update_by_id(self, cmd: BaseSchema, session: AsyncSession) -> BaseSchema:
        """Abstract method for update entity."""
        pass
