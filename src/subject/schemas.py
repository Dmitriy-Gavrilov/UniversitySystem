from pydantic import Field

from src.base.schemas import BaseSchema
from typing import Optional


class SubjectSchema(BaseSchema):
    subject_name: str = Field(max_length=100)

    assignments: Optional["AssignmentSchema"] = None
    statistics: Optional["StatisticsSchema"] = None
