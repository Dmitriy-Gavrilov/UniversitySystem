from sqlalchemy import DateTime, func
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column


class Base(DeclarativeBase):
    __abstract__ = True

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    created_at: Mapped[DateTime] = mapped_column(default=func.now(), nullable=False)
    updated_at: Mapped[DateTime] = mapped_column(default=func.now(), onupdate=func.now(), nullable=False)

# password?
# папки для src и user
# user_id ?
# Статистика
