from fastapi import FastAPI
import uvicorn

from app.config import settings
from app.pkg.common import BaseServer, BaseRouter


class FastAPIServer(BaseServer):
    __app: FastAPI = FastAPI()
    __routers: list[type[BaseRouter]] = []

    def _add_routes(self):
        for router in self.__routers:
            self.__app.include_router(router.get_routers())

    async def run(self):
        self._add_routes()
        config = uvicorn.Config(
            self.__app,
            host=settings.API_HOST,
            port=settings.API_PORT,
            log_level=settings.LOG_LEVEL.lower(),
        )
        server = uvicorn.Server(config)
        await server.serve()
