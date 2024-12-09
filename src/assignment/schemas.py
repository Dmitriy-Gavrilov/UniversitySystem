from pydantic import Field

from src.base.schemas import BaseCreateSchema, BaseModelSchema
from models import WorkType


class BaseAssignmentSchema:
    subject_id: int
    work_type: WorkType
    teacher_id: int
    group_id: int

    subject: list["SubjectSchema"] = Field(default_factory=list)
    teacher: list["TeacherSchema"] = Field(default_factory=list)
    group: list["UniversityGroupSchema"] = Field(default_factory=list)


class AssignmentCreateSchema(BaseCreateSchema, BaseAssignmentSchema):
    pass


class AssignmentSchema(BaseAssignmentSchema, BaseModelSchema):
    pass
