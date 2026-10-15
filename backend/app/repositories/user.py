from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession


from app.models.user import User
from app.models.user_business import UserBusiness

from app.repositories.base import BaseRepository



class UserRepository(BaseRepository):
    def __init__(self, db: AsyncSession):
        super().__init__(db, User)

    async def get_user_businesses(self, user_id:int):
        stmt = (
            select(UserBusiness)
            .where(UserBusiness.user_id == user_id)
        )

        result = await self.db.scalars(stmt)

        return result.all() 