from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.core.database import get_db

from app.services.business import BusinessService

from app.schemes.business import BusinessCreate, BusinessResponse

router = APIRouter(
    prefix="/businesses",
    tags=["Businesses"]
)

@router.get("/{business_id}")
async def get_business(
    business_id:int,
    db: AsyncSession = Depends(get_db),
):
    service = BusinessService(db)
    business = await service.get_business(business_id)
    return business

@router.get("/{business_id}/users")
async def get_business_users(
    business_id: int,
    db: AsyncSession = Depends(get_db),
):
    service = BusinessService(db)

    business_users = await service.get_business_users(business_id)

    return business_users

@router.post("/create", response_model=BusinessResponse, status_code=201)
async def create_business(
    data: BusinessCreate,
    db: AsyncSession = Depends(get_db),
):
    service = BusinessService(db)

    new_business = await service.create_business(data.model_dump())

    await db.commit()
    await db.refresh(new_business)

    return new_business

