from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession

from app.core.database import get_db
from app.schemes.reward import (
    RewardCreate,
    RewardUpdate,
    RewardResponse,
)
from app.services.reward import RewardService


router = APIRouter(
    prefix="/businesses/{business_id}/rewards",
    tags=["Rewards"],
)


@router.post(
    "",
    response_model=RewardResponse,
    status_code=status.HTTP_201_CREATED,
)
async def create_reward(
    business_id: int,
    data: RewardCreate,
    db: AsyncSession = Depends(get_db),
):
    service = RewardService(db)

    try:
        reward = await service.create_reward(
            business_id=business_id,
            data=data.model_dump(),
        )
        await db.commit()
        return reward
    except Exception:
        await db.rollback()
        raise


@router.get("", response_model=list[RewardResponse])
async def get_business_rewards(
    business_id: int,
    active_only: bool = False,
    db: AsyncSession = Depends(get_db),
):
    service = RewardService(db)

    return await service.get_business_rewards(
        business_id=business_id,
        active_only=active_only,
    )


@router.get("/{reward_id}", response_model=RewardResponse)
async def get_reward(
    business_id: int,
    reward_id: int,
    db: AsyncSession = Depends(get_db),
):
    service = RewardService(db)

    try:
        reward = await service.get_reward(reward_id)

        if reward.business_id != business_id:
            raise HTTPException(
                status_code=404,
                detail="Награда не найдена",
            )

        return reward
    except ValueError as exc:
        raise HTTPException(
            status_code=404,
            detail=str(exc),
        ) from exc


@router.patch("/{reward_id}", response_model=RewardResponse)
async def update_reward(
    business_id: int,
    reward_id: int,
    data: RewardUpdate,
    db: AsyncSession = Depends(get_db),
):
    service = RewardService(db)

    try:
        reward = await service.update_reward(
            reward_id=reward_id,
            business_id=business_id,
            data=data.model_dump(exclude_unset=True),
        )
        await db.commit()
        return reward
    except ValueError as exc:
        await db.rollback()
        raise HTTPException(
            status_code=404,
            detail=str(exc),
        ) from exc
    except Exception:
        await db.rollback()
        raise


@router.delete("/{reward_id}", response_model=RewardResponse)
async def deactivate_reward(
    business_id: int,
    reward_id: int,
    db: AsyncSession = Depends(get_db),
):
    service = RewardService(db)

    try:
        reward = await service.deactivate_reward(
            reward_id=reward_id,
            business_id=business_id,
        )
        await db.commit()
        return reward
    except ValueError as exc:
        await db.rollback()
        raise HTTPException(
            status_code=404,
            detail=str(exc),
        ) from exc
    except Exception:
        await db.rollback()
        raise