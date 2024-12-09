from src.base.models import Base
from sqlalchemy import String, Enum, Integer
from sqlalchemy.orm import Mapped, mapped_column
from enum import StrEnum


class UserRole(StrEnum):
    ADMIN = "admin"
    STUDENT = "student"
    TEACHER = "teacher"


class User(Base):
    __tablename__ = "user"

    login: Mapped[str] = mapped_column(String(50), nullable=False, unique=True)
    password: Mapped[str] = mapped_column(String(128), nullable=False)
    role: Mapped[UserRole] = mapped_column(Enum(UserRole, name="user_role"), nullable=False)
