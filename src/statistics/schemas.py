from dataclasses import Field

from src.base.schemas import BaseCreateSchema, BaseModelSchema
from typing import Optional


class BaseStatisticsSchema:
    student_id: int
    subject_id: int
    teacher_id: int
    avg_grades: Optional[float]
    exam_grade: Optional[int]

    student: list["StudentSchema"] = Field(default_factory=list)
    subject: list["SubjectSchema"] = Field(default_factory=list)
    teacher: list["TeacherSchema"] = Field(default_factory=list)


class CreateStatisticsSchema(BaseCreateSchema, BaseStatisticsSchema):
    pass


class StatisticsSchema(BaseModelSchema, BaseStatisticsSchema):
    pass
