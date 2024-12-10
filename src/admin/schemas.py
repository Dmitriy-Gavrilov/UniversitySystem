from src.base.schemas import BaseSchema, BaseModelSchema

from pydantic import Field


class BaseAdminSchema(BaseSchema):
    surname: str = Field(max_length=50)
    name: str = Field(max_length=50)
    patronym: str = Field(max_length=50)


class AdminCreateSchema(BaseAdminSchema):
    pass


class AdminSchema(BaseAdminSchema, BaseModelSchema):
    user_id: int
