from src.base.models import Base
from sqlalchemy import ForeignKey, DateTime, String, func
from sqlalchemy.orm import Mapped, mapped_column, relationship
from datetime import datetime


class Report(Base):
    __tablename__ = "report"

    report_name: Mapped[str] = mapped_column(String(100), nullable=False)
    load_date: Mapped[datetime] = mapped_column(default=func.now(), nullable=False)
    check_date: Mapped[datetime | None] = mapped_column(onupdate=func.now(), nullable=True)
    grade: Mapped[int | None] = mapped_column(nullable=True)
    is_accepted: Mapped[bool] = mapped_column(nullable=False, default=False)
    task_id: Mapped[int] = mapped_column(ForeignKey('task.id', ondelete="CASCADE"))
    student_id: Mapped[int] = mapped_column(ForeignKey('student.id', ondelete="CASCADE"))

    task: Mapped["Task"] = relationship(back_populates="reports", lazy="joined")
    student: Mapped["Student"] = relationship("Student", back_populates="reports", lazy="joined")
