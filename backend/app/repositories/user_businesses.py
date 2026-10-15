from sqlalchemy import update
from sqlalchemy.ext.asyncio import AsyncSession

from app.repositories.base import BaseRepository

from app.models.user_business import UserBusiness


class UserBusinessRepository(BaseRepository):
    def __init__(self, db: AsyncSession):
        super().__init__(db, UserBusiness)
    async def add_visit(self, user_business_id: int):
        stmt = (
            update(UserBusiness)
            .where(UserBusiness.id == user_business_id)
            .values(visits_count = UserBusiness.visits_count + 1)
        )
        await self.db.execute(stmt)
        await self.db.commit()
        

    