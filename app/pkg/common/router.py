from abc import ABCMeta, abstractmethod
from typing import Any

from app.pkg.common import BaseRepository, BaseSchema

__all__ = [
    "BaseRouter",
]


class BaseRouter(metaclass=ABCMeta):
    repository: BaseRepository

    @abstractmethod
    async def get(self, query: BaseSchema, request: Any | None = None):
        pass

    @abstractmethod
    async def post(self, query: BaseSchema, request: Any | None = None):
        pass

    @abstractmethod
    async def delete(self, query: BaseSchema, request: Any | None = None):
        pass

    @abstractmethod
    async def put(self, query: BaseSchema, request: Any | None = None):
        pass

    @staticmethod
    @abstractmethod
    def get_routers() -> Any:
        pass
