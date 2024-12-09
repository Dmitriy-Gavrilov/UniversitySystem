from pydantic import BaseModel, ConfigDict

from datetime import datetime


class BaseCreateSchema(BaseModel):
    config = ConfigDict(from_attributes=True)


class BaseModelSchema(BaseCreateSchema):
    id: int

    created_at: datetime
    updated_at: datetime
