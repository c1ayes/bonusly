from sqlalchemy.ext.asyncio import AsyncSession
from app.repositories.user import UserRepository

class UserService:
    def __init__(self, db:AsyncSession):
        self.user_repository = UserRepository(db)

    async def get_user_businesses(self, user_id: int):
        return await self.user_repository.get_user_businesses(user_id)