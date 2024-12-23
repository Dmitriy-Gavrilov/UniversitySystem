from typing_extensions import Self

from src.base.schemas import BaseSchema, BaseModelSchema
from models import WorkType, Assignment


class BaseAssignmentSchema(BaseSchema):
    subject_id: int
    work_type: WorkType
    teacher_id: int
    group_id: int

    @classmethod
    def from_model(cls, model: Assignment) -> Self:
        return cls(subject_id=model.subject_id, )


# Лекции и лабы

class AssignmentCreateSchema(BaseAssignmentSchema):
    pass


class AssignmentSchema(BaseAssignmentSchema, BaseModelSchema):
    pass
