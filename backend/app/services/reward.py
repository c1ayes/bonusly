from sqlalchemy.ext.asyncio import AsyncSession

from app.models.reward import Reward
from app.repositories.reward import RewardRepository


class RewardService:
    def __init__(self, db: AsyncSession):
        self.repository = RewardRepository(db)

    async def create_reward(
        self,
        business_id: int,
        data: dict,
    ) -> Reward:
        data["business_id"] = business_id

        return await self.repository.create(data)

    async def get_reward(self, reward_id: int) -> Reward:
        reward = await self.repository.get_by_id(reward_id)

        if not reward:
            raise ValueError("Награда не найдена")

        return reward

    async def get_business_rewards(
        self,
        business_id: int,
        active_only: bool = False,
    ) -> list[Reward]:
        return await self.repository.get_by_business(
            business_id=business_id,
            active_only=active_only,
        )

    async def update_reward(
        self,
        reward_id: int,
        business_id: int,
        data: dict,
    ) -> Reward:
        reward = await self.get_reward(reward_id)

        if reward.business_id != business_id:
            raise ValueError("Награда принадлежит другому бизнесу")

        for key, value in data.items():
            setattr(reward, key, value)

        await self.repository.db.flush()
        await self.repository.db.refresh(reward)

        return reward

    async def deactivate_reward(
        self,
        reward_id: int,
        business_id: int,
    ) -> Reward:
        reward = await self.get_reward(reward_id)

        if reward.business_id != business_id:
            raise ValueError("Награда принадлежит другому бизнесу")

        reward.is_active = False

        await self.repository.db.flush()
        await self.repository.db.refresh(reward)

        return reward