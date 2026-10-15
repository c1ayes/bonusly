from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession


class BaseRepository:
    def __init__(self, db: AsyncSession, model):
        self.db = db
        self.model = model

    async def get_by_id(self, entity_id: int):
        return await self.db.get(self.model, entity_id)

    async def get_all(self):
        stmt = select(self.model)
        result = await self.db.scalars(stmt)
        return result.all()

    async def create(self, data: dict):
        entity = self.model(**data)

        self.db.add(entity)

        await self.db.flush()
        await self.db.refresh(entity)

        return entity

    async def delete(self, entity):
        await self.db.delete(entity)
        await self.db.flush()