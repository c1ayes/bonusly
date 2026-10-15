from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.repositories.base import BaseRepository

from app.models.business import Business
from app.models.user_business import UserBusiness


class BusinessRepository(BaseRepository):
    def __init__(self, db:AsyncSession):
        super().__init__(db, Business)

    async def get_business_users(self, business_id:int):
        stmt = (
            select(UserBusiness)
            .where(UserBusiness.business_id == business_id)
        )
        result = await self.db.scalars(stmt)
        return result.all()