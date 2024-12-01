from src.base.models import Base
from sqlalchemy import String, Enum
from sqlalchemy.orm import Mapped, mapped_column


class User(Base):
    __tablename__ = "user"

    user_id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    login: Mapped[str] = mapped_column(String(50), nullable=False, unique=True)
    password: Mapped[str] = mapped_column(String(128), nullable=False)
    role: Mapped[str] = mapped_column(Enum("admin", "student", "teacher", name="user_role"), nullable=False)
