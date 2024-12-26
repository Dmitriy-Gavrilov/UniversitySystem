from src.base.schemas import BaseSchema, BaseModelSchema
from pydantic import Field


class BaseTeacherSchema(BaseSchema):
    surname: str = Field(max_length=50)
    name: str = Field(max_length=50)
    patronym: str = Field(max_length=50)


class CreateTeacherSchema(BaseTeacherSchema):
    pass


class TeacherSchema(BaseTeacherSchema, BaseModelSchema):
    user_id: int


class ResponseTeacherSchema(TeacherSchema):
    subjects: list[str]
