from src.base.models import Base
from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from src.assignment.models import Assignment


class UniversityGroup(Base):
    __tablename__ = "university_group"

    group_name: Mapped[str] = mapped_column(String(25), nullable=False, unique=True)

    students: Mapped[list["Student"]] = relationship("Student", back_populates="group", lazy="joined",
                                                     cascade="all, delete")
    assignments: Mapped[list[Assignment]] = relationship("Assignment", back_populates="group", lazy="joined",
                                                         cascade="all, delete")
