from datetime import datetime

from typing_extensions import Self

from src.base.schemas import BaseSchema, BaseModelSchema
from models import WorkType, Assignment


class BaseAssignmentSchema(BaseSchema):
    subject_id: int
    work_type: WorkType
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


# Дописать лекции и лабы?

class AssignmentCreateSchema(BaseAssignmentSchema):
    pass


class AssignmentSchema(BaseAssignmentSchema, BaseModelSchema):
    pass
