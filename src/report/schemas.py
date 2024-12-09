from src.base.schemas import BaseCreateSchema, BaseModelSchema
from pydantic import Field
from datetime import datetime


class BaseReportSchema:
    report_name: str = Field(max_length=100)
    load_date: datetime
    accept_date: datetime | None
    grade: int | None = Field(ge=0, le=100)
    task_id: int
    student_id: int

    task: list["TaskSchema"] = Field(default_factory=list)


class CreateReportSchema(BaseCreateSchema, BaseReportSchema):
    pass


class ReportSchema(BaseModelSchema, BaseReportSchema):
    pass
