from src.base.schemas import BaseSchema, BaseModelSchema


class BaseStatisticsSchema(BaseSchema):
    student_id: int
    subject_id: int
    teacher_id: int
    avg_grades: float | None
    exam_grade: int | None


class CreateStatisticsSchema(BaseStatisticsSchema):
    pass


class StatisticsSchema(BaseStatisticsSchema, BaseModelSchema):
    pass
