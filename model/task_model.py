from sqlalchemy import String, Text, Engine, select
from sqlalchemy.orm import Mapped, mapped_column, DeclarativeBase, Session


class BaseModel(DeclarativeBase):
    pass


class TaskModel(BaseModel):
    __tablename__ = "tasks"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    title: Mapped[str] = mapped_column(String(100))
    description: Mapped[str | None] = mapped_column(Text, nullable=True, default=None)
    is_completed: Mapped[bool] = mapped_column(default=False)