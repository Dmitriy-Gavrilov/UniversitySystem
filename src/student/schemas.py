from src.base.schemas import BaseSchema, BaseModelSchema
from pydantic import Field


class BaseStudentSchema(BaseSchema):
    surname: str = Field(max_length=50)
    name: str = Field(max_length=50)
    patronym: str = Field(max_length=50)
    group_id: int


class CreateStudentSchema(BaseStudentSchema):
    pass


class StudentSchema(BaseStudentSchema, BaseModelSchema):
    user_id: int
