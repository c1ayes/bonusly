from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.models.reward import Reward
from app.repositories.base import BaseRepository


class RewardRepository(BaseRepository):
    def __init__(self, db: AsyncSession):
        super().__init__(db, Reward)

    async def get_by_business(
        self,
        business_id: int,
        active_only: bool = False,
    ) -> list[Reward]:
        stmt = select(Reward).where(
            Reward.business_id == business_id
        )

        if active_only:
            stmt = stmt.where(Reward.is_active.is_(True))

        stmt = stmt.order_by(Reward.visits_required)

        result = await self.db.scalars(stmt)

        return list(result.all())