from pydantic import BaseModel, ConfigDict


class UserBusinessCreate(BaseModel):
    user_id: int
    business_id: int

class UserBusinessResponse(BaseModel):
    id: int
    user_id: int
    business_id: int
    visits_count: int
    
    model_config = ConfigDict(from_attributes=True)