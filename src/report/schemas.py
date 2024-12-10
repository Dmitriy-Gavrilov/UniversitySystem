from src.base.schemas import BaseSchema, BaseModelSchema
from pydantic import Field
from datetime import datetime


class BaseReportSchema(BaseSchema):
    report_name: str = Field(max_length=100)
    load_date: datetime
    accept_date: datetime | None
    grade: int | None = Field(ge=0, le=100)
    task_id: int
    student_id: int


class CreateReportSchema(BaseReportSchema):
    pass


class ReportSchema(BaseReportSchema, BaseModelSchema):
    pass
