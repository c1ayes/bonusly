from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession

from app.schemes.user_business import UserBusinessCreate, UserBusinessResponse

from app.core.database import get_db

from app.services.user_business import UserBusinessService

router = APIRouter(
    prefix="/userbusinesses",
    tags=["UserBusinesses"],
)

@router.post("/", response_model=UserBusinessResponse, status_code=201)
async def create_user_business(
    data: UserBusinessCreate,
    db: AsyncSession = Depends(get_db)
):
    service = UserBusinessService(db)

    new_user_business = await service.create_user_business(data.model_dump())
    await db.commit()
    await db.refresh(new_user_business)

    return new_user_business

@router.patch("/")
async def add_visit(
    user_business_id: int,
    db: AsyncSession = Depends(get_db)
):
    service = UserBusinessService(db)


    user_business = await service.get_by_id(user_business_id)

    if user_business is None:
        raise HTTPException(
            status_code=404,
            detail="UserBusiness not found"
        )

    await service.add_visit(user_business_id)
    user_business = await service.get_by_id(user_business_id)

    return user_business

@router.get("/")
async def get_by_id(
    user_business_id:int,
    db: AsyncSession = Depends(get_db)
):
    service = UserBusinessService(db)

    user_business = await service.get_by_id(user_business_id)
    return user_business