from datetime import datetime

from pydantic import BaseModel, ConfigDict


class RewardRedemptionResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    user_business_id: int
    reward_id: int
    visits_spent: int
    redeemed_at: datetime