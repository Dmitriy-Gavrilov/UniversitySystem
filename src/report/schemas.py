from src.base.schemas import BaseSchema, BaseModelSchema
from pydantic import Field
from datetime import datetime


class BaseReportSchema(BaseSchema):
    report_name: str = Field(max_length=100)
    task_id: int
    student_id: int


class CreateReportSchema(BaseReportSchema):
    pass


class ReportSchema(BaseReportSchema, BaseModelSchema):
    load_date: datetime
    check_date: datetime | None
    grade: int | None
    is_accepted: bool


class UpdateReportSchema(BaseSchema):
    is_accepted: bool | None = None
    grade: int | None = Field(ge=0, le=100, default=None)
