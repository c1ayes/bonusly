from pydantic import BaseModel, ConfigDict, Field


class RewardCreate(BaseModel):
    name: str = Field(min_length=1, max_length=100)
    description: str | None = None
    visits_required: int = Field(gt=0)


class RewardUpdate(BaseModel):
    name: str | None = Field(
        default=None,
        min_length=1,
        max_length=100,
    )
    description: str | None = None
    visits_required: int | None = Field(default=None, gt=0)
    is_active: bool | None = None


class RewardResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    business_id: int
    name: str
    description: str | None
    visits_required: int
    is_active: bool