from src.base.models import Base
from sqlalchemy import ForeignKey, Enum
from sqlalchemy.orm import Mapped, mapped_column, relationship


class Assignment(Base):
    __tablename__ = "assignment"

    subject_id: Mapped[int] = mapped_column(ForeignKey('subject.id'), nullable=False)
    work_type: Mapped[str] = mapped_column(Enum("lecture", "laboratory_work", "exam", name="work_type"), nullable=False)
    teacher_id: Mapped[int] = mapped_column(ForeignKey('teacher.id'), nullable=False)
    group_id: Mapped[int] = mapped_column(ForeignKey('university_group.id'), nullable=False)

    subject: Mapped["Subject"] = relationship(lazy="joined")
    teacher: Mapped["Teacher"] = relationship(lazy="joined")
    group: Mapped["UniversityGroup"] = relationship(lazy="joined")
