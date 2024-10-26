from abc import ABCMeta, abstractmethod
from typing import Any

from app.pkg.common import BaseRepository, BaseSchema

__all__ = [
    "BaseRouter",
]


class BaseRouter(metaclass=ABCMeta):
    repository: BaseRepository

    @abstractmethod
    async def get(self, request: Any, query: BaseSchema):
        pass

    @abstractmethod
    async def post(self, request: Any, query: BaseSchema):
        pass

    @abstractmethod
    async def delete(self, request: Any, query: BaseSchema):
        pass

    @abstractmethod
    async def put(self, request: Any, query: BaseSchema):
        pass

    @staticmethod
    @abstractmethod
    def get_routers() -> Any:
        pass
