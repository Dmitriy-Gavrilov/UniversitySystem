from src.base.models import Base
from sqlalchemy import ForeignKey, Float, Integer
from sqlalchemy.orm import Mapped, mapped_column, relationship

from src.teacher.models import Teacher


class Statistics(Base):
    __tablename__ = "statistics"

    student_id: Mapped[int] = mapped_column(ForeignKey('student.id'), nullable=False)
    subject_id: Mapped[int] = mapped_column(ForeignKey('subject.id'), nullable=False)
    teacher_id: Mapped[int] = mapped_column(ForeignKey('teacher.id'), nullable=False)
    avg_grades: Mapped[float | None] = mapped_column(Float, nullable=True)
    exam_grade: Mapped[int | None] = mapped_column(Integer, nullable=True)

    student: Mapped["Student"] = relationship("Student", back_populates="statistics", lazy="joined")
    teacher: Mapped[Teacher] = relationship("Teacher", back_populates="statistics", lazy="joined")
    subject: Mapped["Subject"] = relationship("Subject", back_populates="statistics", lazy="joined")
