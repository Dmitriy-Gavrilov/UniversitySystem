from src.base.models import Base
from sqlalchemy import ForeignKey, Enum
from sqlalchemy.orm import Mapped, mapped_column, relationship
from enum import StrEnum

from src.subject.models import Subject


class WorkType(StrEnum):
    LECTURE = "lecture"
    LABORATORY_WORK = "laboratory_work"
    EXAM = "exam"


class Assignment(Base):
    __tablename__ = "assignment"

    subject_id: Mapped[int] = mapped_column(ForeignKey('subject.id'), nullable=False)
    work_type: Mapped[WorkType] = mapped_column(Enum(WorkType, name="work_type"), nullable=False)
    teacher_id: Mapped[int] = mapped_column(ForeignKey('teacher.id'), nullable=False)
    group_id: Mapped[int] = mapped_column(ForeignKey('university_group.id'), nullable=False)

    subject: Mapped[Subject] = relationship("Subject", back_populates="assignments", lazy="joined")
    teacher: Mapped["Teacher"] = relationship("Teacher", back_populates="assignments", lazy="joined")
    group: Mapped["UniversityGroup"] = relationship("UniversityGroup", back_populates="assignments", lazy="joined")
