from src.base.models import Base
from sqlalchemy import String, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship


class Student(Base):
    __tablename__ = "student"

    user_id: Mapped[int] = mapped_column(ForeignKey('user.id'), nullable=False)
    surname: Mapped[str] = mapped_column(String(50), nullable=False)
    name: Mapped[str] = mapped_column(String(50), nullable=False)
    patronym: Mapped[str] = mapped_column(String(50), nullable=False)
    group_id: Mapped[int] = mapped_column(ForeignKey('university_group.id'))

    group: Mapped["UniversityGroup"] = relationship(back_populates="students", lazy="joined")
    statistics: Mapped[list["Statistics"]] = relationship("Statistics", back_populates="student")

