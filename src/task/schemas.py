from src.base.schemas import BaseCreateSchema, BaseModelSchema
from pydantic import Field


class BaseTaskSchema:
    task_name: str = Field(max_length=100)
    points: int = Field(ge=0, le=100)
    assignment_id: int

    reports: list["ReportSchema"] = Field(default_factory=list)


class CreateTaskSchema(BaseCreateSchema, BaseTaskSchema):
    pass


class TaskSchema(BaseModelSchema, BaseTaskSchema):
    pass
