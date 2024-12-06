import asyncio
from typing import Generic, TypeVar, Type
from sqlalchemy import select, delete
from sqlalchemy.ext.asyncio import AsyncSession

M = TypeVar('M')


class Repository(Generic[M]):
    def __init__(self, model: Type[M], session: AsyncSession):
        self.session = session
        self.Model = model

    async def create(self, new_object: M) -> None:
        async with asyncio.Lock():
            await self._create(new_object)

    async def _create(self, new_object: M) -> None:
        async with self.session:
            self.session.add(new_object)
            await self.session.commit()

    async def get(self, **kwargs) -> M:
        async with asyncio.Lock():
            await self._get(**kwargs)

    async def _get(self, **kwargs) -> M:
        async with self.session:
            statement = select(self.Model).filter_by(**kwargs)
            result = await self.session.execute(statement)
            await result.scalars().first()

    async def get_all(self) -> list[M]:
        async with self.session:
            statement = select(self.Model)
            result = await self.session.execute(statement)
            return result.scalars().all()

    async def delete(self, object_id: int) -> None:
        async with asyncio.Lock():
            await self._delete(object_id)

    async def _delete(self, object_id: int) -> None:
        async with self.session:
            try:
                statement = delete(self.Model).where(self.Model.id == object_id)
                await self.session.execute(statement)
                await self.session.commit()
            except (Exception,) as exc:
                await self.session.rollback()
                raise exc
