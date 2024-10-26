from fastapi import Depends

from app.config import get_logger
from app.pkg.common import BaseRepository
from app.pkg.models import PostsModel
from app.pkg.schema import (
    GetPostsByIDSchema,
    PostsSchema,
    CreatePostsSchema,
    DeletePostsByIDSchema,
    UpdatePostsSchema,
)
from app.pkg.session import get_async_session
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from sqlalchemy import delete, update

logger = get_logger()

__all__ = [
    "PostsRepository",
]


class PostsRepository(BaseRepository):
    async def _check_exist_by_id(
        self,
        query: GetPostsByIDSchema,
        session: AsyncSession,
    ) -> PostsModel | None:
        result = await session.execute(
            select(PostsModel).where(PostsModel.id == query.id)
        )
        blog_message = await result.scalar_one_or_none()
        if blog_message is None:
            return None
        return blog_message

    async def get_by_id(
        self,
        query: GetPostsByIDSchema,
        session: AsyncSession = Depends(get_async_session),
    ) -> PostsSchema | None:
        blog_message = await self._check_exist_by_id(query, session)
        if blog_message is None:
            return None
        return PostsSchema.model_validate(blog_message)

    async def create(
        self,
        cmd: CreatePostsSchema,
        session: AsyncSession = Depends(get_async_session),
    ) -> PostsSchema | None:
        blog_message = await self._check_exist_by_id(cmd, session)
        if blog_message is not None:
            return None
        model = PostsModel()
        session.add(model)
        await session.commit()
        return PostsSchema.model_validate(model)

    async def delete_by_id(
        self,
        cmd: DeletePostsByIDSchema,
        session: AsyncSession = Depends(get_async_session),
    ) -> DeletePostsByIDSchema | None:
        result_check = await self._check_exist_by_id(cmd, session)
        if result_check is None:
            return None
        result = delete(PostsModel).where(PostsModel.id == cmd.id)
        await session.execute(result)
        await session.commit()
        return cmd

    async def update_by_id(
        self,
        cmd: UpdatePostsSchema,
        session: AsyncSession = Depends(get_async_session),
    ) -> PostsSchema | None:
        result_check = await self._check_exist_by_id(cmd, session)
        if result_check is None:
            return None
        stmt = (
            update(PostsModel)
            .where(PostsModel.id == cmd.id)
            .values(title=cmd.title, content=cmd.content)
        )
        await session.execute(stmt)
        await session.commit()
        return PostsSchema.model_validate(cmd)
