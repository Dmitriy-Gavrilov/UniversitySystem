from src.base.schemas import BaseCreateSchema, BaseModelSchema
from pydantic import Field


class BaseTeacherSchema:
    surname: str = Field(max_length=50)
    name: str = Field(max_length=50)
    patronym: str = Field(max_length=50)

    assignments: list["AssignmentSchema"] = Field(default_factory=list)
    statistics: list["StatisticsSchema"] = Field(default_factory=list)


class CreateTeacherSchema(BaseCreateSchema, BaseTeacherSchema):
    pass


class TeacherSchema(BaseModelSchema, BaseTeacherSchema):
    user_id: int
