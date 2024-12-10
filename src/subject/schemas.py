from pydantic import Field

from src.base.schemas import BaseSchema, BaseModelSchema


class BaseSubjectSchema(BaseSchema):
    subject_name: str = Field(max_length=100)


class CreateSubjectSchema(BaseSubjectSchema):
    pass


class SubjectSchema(BaseSubjectSchema, BaseModelSchema):
    pass
