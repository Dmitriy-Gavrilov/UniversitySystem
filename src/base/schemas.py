from pydantic import BaseModel, ConfigDict

from datetime import datetime


class BaseSchema(BaseModel):
    class Config:
        from_attributes = True


class BaseCreateSchema(BaseSchema):
    pass


class BaseModelSchema(BaseCreateSchema):
    id: int

    created_at: datetime
    updated_at: datetime
