from src.base.schemas import BaseCreateSchema, BaseModelSchema
from pydantic import Field


class BaseStudentSchema:
    surname: str = Field(max_length=50)
    name: str = Field(max_length=50)
    patronym: str = Field(max_length=50)
    group_id: int

    group: list["GroupSchema"] = Field(default_factory=list)
    statistics: list["StatisticsSchema"] = Field(default_factory=list)


class CreateStudentSchema(BaseCreateSchema, BaseStudentSchema):
    pass


class StudentSchema(BaseModelSchema, BaseStudentSchema):
    user_id: int
