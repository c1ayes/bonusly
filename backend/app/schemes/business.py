from pydantic import BaseModel, ConfigDict


class BusinessCreate(BaseModel):
    name: str


class BusinessResponse(BaseModel):
    id: int
    name: str

    model_config = ConfigDict(from_attributes=True)