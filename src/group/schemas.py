from src.base.schemas import BaseModelSchema, BaseSchema
from pydantic import Field


class BaseGroupSchema(BaseSchema):
    group_name: str = Field(max_length=25)


class GroupCreateSchema(BaseGroupSchema):
    pass


class GroupSchema(BaseGroupSchema, BaseModelSchema):
    pass
