from src.base.models import Base
from sqlalchemy import String, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship


class Teacher(Base):
    __tablename__ = "teacher"

    user_id: Mapped[int] = mapped_column(ForeignKey('user.id',  ondelete="CASCADE"), nullable=False)
    surname: Mapped[str] = mapped_column(String(50), nullable=False)
    name: Mapped[str] = mapped_column(String(50), nullable=False)
    patronym: Mapped[str] = mapped_column(String(50), nullable=False)

    assignments: Mapped[list["Assignment"]] = relationship("Assignment", back_populates="teacher", cascade="all, delete")
    statistics: Mapped[list["Statistics"]] = relationship("Statistics", back_populates="teacher")
