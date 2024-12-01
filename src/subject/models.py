from src.base.models import Base
from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column


class Subject(Base):
    __tablename__ = "subject"

    subject_name: Mapped[str] = mapped_column(String(100), nullable=False, unique=True)
