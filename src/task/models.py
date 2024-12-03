from src.base.models import Base
from sqlalchemy import ForeignKey, String
from sqlalchemy.orm import Mapped, mapped_column, relationship


class Task(Base):
    __tablename__ = "task"

    task_name: Mapped[str] = mapped_column(String(100), nullable=False)
    points: Mapped[int] = mapped_column(nullable=False)
    assignment_id: Mapped[int] = mapped_column(ForeignKey('assignment.id'))

    reports: Mapped[list["Report"]] = relationship(back_populates="task", lazy="joined")
