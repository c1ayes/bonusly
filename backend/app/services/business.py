from sqlalchemy.ext.asyncio import AsyncSession

from app.repositories.business import BusinessRepository


class BusinessService:
    def __init__(self, db:AsyncSession):
        self.business_repository = BusinessRepository(db)
        
    async def get_business(self, business_id):
        return await self.business_repository.get_by_id(business_id)
    
    async def create_business(self, data:dict):
        return await self.business_repository.create(data)
    
    async def get_business_users(self, business_id:int):
        return await self.business_repository.get_business_users(business_id)
    