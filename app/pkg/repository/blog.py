from fastapi import Depends

from app.config import get_logger
from app.pkg.common import BaseRepository
from app.pkg.models import BlogModel
from app.pkg.schema import (
    GetBlogByIDSchema,
    BlogSchema,
    CreateBlogSchema,
    DeleteBlogByIDSchema,
    UpdateBlogSchema,
)
from app.pkg.session import get_async_session
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from sqlalchemy import delete, update

logger = get_logger()

__all__ = [
    "BlogRepository",
]


class BlogRepository(BaseRepository):
    async def _check_exist_by_id(
        self,
        query: GetBlogByIDSchema,
        session: AsyncSession,
    ) -> BlogModel | None:
        result = await session.execute(
            select(BlogModel).where(BlogModel.id == query.id)
        )
        blog_message = await result.scalar_one_or_none()
        if blog_message is None:
            return None
        return blog_message

    async def get_by_id(
        self,
        query: GetBlogByIDSchema,
        session: AsyncSession = Depends(get_async_session),
    ) -> BlogSchema | None:
        blog_message = await self._check_exist_by_id(query, session)
        if blog_message is None:
            return None
        return BlogSchema.model_validate(blog_message)

    async def create(
        self,
        cmd: CreateBlogSchema,
        session: AsyncSession = Depends(get_async_session),
    ) -> BlogSchema | None:
        blog_message = await self._check_exist_by_id(cmd, session)
        if blog_message is not None:
            return None
        model = BlogModel()
        session.add(model)
        await session.commit()
        return BlogSchema.model_validate(model)

    async def delete_by_id(
        self,
        cmd: DeleteBlogByIDSchema,
        session: AsyncSession = Depends(get_async_session),
    ) -> DeleteBlogByIDSchema | None:
        result_check = await self._check_exist_by_id(cmd, session)
        if result_check is None:
            return None
        result = delete(BlogModel).where(BlogModel.id == cmd.id)
        await session.execute(result)
        await session.commit()
        return cmd

    async def update_by_id(
        self,
        cmd: UpdateBlogSchema,
        session: AsyncSession = Depends(get_async_session),
    ) -> BlogSchema | None:
        result_check = await self._check_exist_by_id(cmd, session)
        if result_check is None:
            return None
        stmt = (
            update(BlogModel)
            .where(BlogModel.id == cmd.id)
            .values(title=cmd.title, content=cmd.content)
        )
        await session.execute(stmt)
        await session.commit()
        return BlogSchema.model_validate(cmd)
