from src.base.models import Base
from task import Task
from sqlalchemy import ForeignKey, DateTime, String, func
from sqlalchemy.orm import Mapped, mapped_column, relationship


class Report(Base):
    __tablename__ = "report"

    report_id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    report_name: Mapped[str] = mapped_column(String(100), nullable=False)
    load_date: Mapped[DateTime] = mapped_column(default=func.now(), nullable=False)
    accept_date: Mapped[DateTime | None] = mapped_column(nullable=True)
    grade: Mapped[int | None] = mapped_column(nullable=True)
    task_id: Mapped[int] = mapped_column(ForeignKey('task.id'))
    student_id: Mapped[int] = mapped_column(ForeignKey('student.id'))

    task: Mapped["Task"] = relationship(back_populates="reports", lazy="joined")
