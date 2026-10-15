from sqlalchemy.ext.asyncio import AsyncSession

from app.repositories.user_businesses import UserBusinessRepository


class UserBusinessService:
    def __init__(self, db:AsyncSession):
        self.user_business_repository = UserBusinessRepository(db)

    async def get_by_id(self, id):
        return await self.user_business_repository.get_by_id(id)
    async def create_user_business(self, data:dict):
        return await self.user_business_repository.create(data)

    async def add_visit(self, user_business_id:int):
        return await self.user_business_repository.add_visit(user_business_id)
