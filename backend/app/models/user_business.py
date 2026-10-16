from sqlalchemy import ForeignKey, UniqueConstraint
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.core.database import Base

class UserBusiness(Base):
    __tablename__ = "user_businesses"

    __table_args__ = (
        UniqueConstraint(
            "user_id",
            "business_id",
            name="uq_user_business",
        ),
    )

    id: Mapped[int] = mapped_column(
        primary_key=True,
    )
  
    user_id: Mapped[int] = mapped_column(
        ForeignKey("users.id"),
        index=True
    )
    business_id:Mapped[int] = mapped_column(
        ForeignKey("businesses.id"),
        index=True
    )
    visits_count:Mapped[int] = mapped_column(default=0)

    user: Mapped["User"] = relationship(
        back_populates="user_businesses"
    )
    business: Mapped["Business"] = relationship(
        back_populates="user_businesses"
    )
    redemptions: Mapped[list["RewardRedemption"]] = relationship(
        back_populates="user_business"
    )