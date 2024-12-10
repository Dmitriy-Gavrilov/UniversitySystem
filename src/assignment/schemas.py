from src.base.schemas import BaseSchema, BaseModelSchema
from models import WorkType


class BaseAssignmentSchema(BaseSchema):
    subject_id: int
    work_type: WorkType
    teacher_id: int
    group_id: int


class AssignmentCreateSchema(BaseAssignmentSchema):
    pass


class AssignmentSchema(BaseAssignmentSchema, BaseModelSchema):
    pass
