from src.base.schemas import BaseCreateSchema, BaseModelSchema

from pydantic import Field


class BaseAdminSchema:
    surname: str = Field(max_length=50)
    name: str = Field(max_length=50)
    patronym: str = Field(max_length=50)


class AdminCreateSchema(BaseCreateSchema, BaseAdminSchema):
    pass


class AdminSchema(BaseAdminSchema, BaseModelSchema):
    user_id: int
