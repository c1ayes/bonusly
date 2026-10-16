from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.models.reward_redemption import RewardRedemption
from app.models.reward import Reward
from app.models.user_business import UserBusiness
from app.repositories.reward_redemption import (
    RewardRedemptionRepository,
)


class RewardRedemptionService:
    def __init__(self, db: AsyncSession):
        self.db = db
        self.repository = RewardRedemptionRepository(db)

    async def redeem_reward(
        self,
        user_business_id: int,
        reward_id: int,
    ) -> RewardRedemption:
        async with self.db.begin_nested():
            # Блокируем баланс, чтобы избежать двойного списания.
            stmt = (
                select(UserBusiness)
                .where(UserBusiness.id == user_business_id)
                .with_for_update()
            )
            result = await self.db.execute(stmt)
            user_business = result.scalar_one_or_none()

            if not user_business:
                raise ValueError("Пользователь не найден в этом бизнесе")

            reward = await self.db.get(Reward, reward_id)

            if not reward:
                raise ValueError("Награда не найдена")

            if not reward.is_active:
                raise ValueError("Награда неактивна")

            if reward.business_id != user_business.business_id:
                raise ValueError("Награда принадлежит другому бизнесу")

            if user_business.visits_count < reward.visits_required:
                raise ValueError("Недостаточно посещений")

            visits_spent = reward.visits_required
            user_business.visits_count -= visits_spent

            redemption = RewardRedemption(
                user_business_id=user_business.id,
                reward_id=reward.id,
                visits_spent=visits_spent,
            )

            self.db.add(redemption)
            await self.db.flush()
            await self.db.refresh(redemption)

        return redemption

    async def get_redemption_history(
        self,
        user_business_id: int,
    ) -> list[RewardRedemption]:
        return await self.repository.get_by_user_business(
            user_business_id=user_business_id,
        )