from src.base.schemas import BaseSchema, BaseModelSchema
from pydantic import Field


class BaseTaskSchema(BaseSchema):
    task_name: str = Field(max_length=100)
    points: int = Field(ge=0, le=100)
    assignment_id: int


class CreateTaskSchema(BaseTaskSchema):
    pass


class TaskSchema(BaseTaskSchema, BaseModelSchema):
    pass


class ResponseTaskSchema(TaskSchema):
    subject_name: str
    teacher_surname: str
    teacher_name: str
    teacher_patronym: str
    group_name: str
