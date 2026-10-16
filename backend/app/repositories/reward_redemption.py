from sqlalchemy import select, desc
from sqlalchemy.ext.asyncio import AsyncSession

from app.models.reward_redemption import RewardRedemption
from app.repositories.base import BaseRepository


class RewardRedemptionRepository(BaseRepository):
    def __init__(self, db: AsyncSession):
        super().__init__(db, RewardRedemption)

    async def get_by_user_business(
        self,
        user_business_id: int,
    ) -> list[RewardRedemption]:
        stmt = (
            select(RewardRedemption)
            .where(
                RewardRedemption.user_business_id
                == user_business_id
            )
            .order_by(desc(RewardRedemption.redeemed_at))
        )

        result = await self.db.scalars(stmt)

        return list(result.all())