from datetime import datetime, date, time

from typing_extensions import Self

from src.base.schemas import BaseSchema, BaseModelSchema
from src.assignment.models import WorkType, Assignment


class BaseAssignmentSchema(BaseSchema):
    work_type: WorkType

    @classmethod
    async def to_datetime(cls, d: date, t: time):
        return datetime.combine(d, t)


# Дописать лекции и лабы?

class AssignmentCreateSchema(BaseAssignmentSchema):
    date: date
    time: time


class AssignmentSchema(BaseAssignmentSchema, BaseModelSchema):
    subject_id: int
    teacher_id: int
    group_id: int
    time: datetime

    @classmethod
    def from_model(cls, model: Assignment) -> Self:
        return cls(
            subject_id=model.subject_id,
            work_type=model.work_type,
            teacher_id=model.teacher_id,
            group_id=model.group_id,
            time=model.time)


class ResponseAssignmentSchema(AssignmentSchema):
    subject_name: str
    teacher_surname: str
    teacher_name: str
    teacher_patronym: str
    group_name: str
