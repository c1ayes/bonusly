from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession

from app.core.database import get_db
from app.schemes.reward_redemption import RewardRedemptionResponse
from app.services.reward_redemption import RewardRedemptionService


router = APIRouter(
    prefix="/user-businesses/{user_business_id}/redemptions",
    tags=["Reward redemptions"],
)


@router.post(
    "/{reward_id}",
    response_model=RewardRedemptionResponse,
    status_code=status.HTTP_201_CREATED,
)
async def redeem_reward(
    user_business_id: int,
    reward_id: int,
    db: AsyncSession = Depends(get_db),
):
    service = RewardRedemptionService(db)

    try:
        redemption = await service.redeem_reward(
            user_business_id=user_business_id,
            reward_id=reward_id,
        )
        await db.commit()
        return redemption
    except ValueError as exc:
        await db.rollback()
        raise HTTPException(
            status_code=400,
            detail=str(exc),
        ) from exc
    except Exception:
        await db.rollback()
        raise


@router.get("", response_model=list[RewardRedemptionResponse])
async def get_redemption_history(
    user_business_id: int,
    db: AsyncSession = Depends(get_db),
):
    service = RewardRedemptionService(db)

    return await service.get_redemption_history(
        user_business_id=user_business_id,
    )