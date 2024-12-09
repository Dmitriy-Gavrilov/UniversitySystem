from src.base.schemas import BaseModelSchema, BaseCreateSchema
from pydantic import Field


class BaseGroupSchema:
    group_name: str = Field(max_length=25)

    students: list["StudentSchema"] = Field(default_factory=list)
    assignments: list["AssignmentSchema"] = Field(default_factory=list)


class GroupCreateSchema(BaseCreateSchema, BaseGroupSchema):
    pass


class GroupSchema(BaseModelSchema, BaseGroupSchema):
    pass
