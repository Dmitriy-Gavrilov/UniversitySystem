from src.base.models import Base
from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from src.statistics.models import Statistics


class Subject(Base):
    __tablename__ = "subject"

    subject_name: Mapped[str] = mapped_column(String(100), nullable=False, unique=True)

    assignments: Mapped[list["Assignment"]] = relationship("Assignment", back_populates="subject", cascade="all, delete")
    statistics: Mapped[list[Statistics]] = relationship("Statistics", back_populates="subject", cascade="all, delete")
