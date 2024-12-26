from src.base.models import Base
from sqlalchemy import String, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column


class Administrator(Base):
    __tablename__ = "administrator"

    user_id: Mapped[int] = mapped_column(ForeignKey('user.id', ondelete="CASCADE"), nullable=False)
    surname: Mapped[str] = mapped_column(String(50), nullable=False)
    name: Mapped[str] = mapped_column(String(50), nullable=False)
    patronym: Mapped[str] = mapped_column(String(50), nullable=False)
