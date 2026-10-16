from sqlalchemy import ForeignKey, func, DateTime
from sqlalchemy.orm import Mapped, mapped_column, relationship
from datetime import datetime

from app.core.database import Base

class RewardRedemption(Base):
    __tablename__ = "reward_redemptions"

    id: Mapped[int] = mapped_column(primary_key=True)

    user_business_id: Mapped[int] = mapped_column(
        ForeignKey("user_businesses.id"),
        index=True,
    )
    reward_id: Mapped[int] = mapped_column(
        ForeignKey("rewards.id"),
        index=True,
    )

    visits_spent: Mapped[int] = mapped_column(nullable=False)
    redeemed_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        server_default=func.now(),
        nullable=False,
    )

    user_business: Mapped["UserBusiness"] = relationship(
        back_populates="redemptions"
    )

    reward: Mapped["Reward"] = relationship(
        back_populates="redemptions"
    )