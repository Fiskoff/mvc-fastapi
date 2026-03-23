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


class TaskRepository:
    def __init__(self, engine: Engine) -> None:
        self.engine = engine

    def create(self, task_dict: dict) -> TaskModel:
        new_task = TaskModel(**task_dict)
        with Session(self.engine) as session:
            session.add(new_task)
            session.commit()
            session.refresh(new_task)
            return new_task

    def get_all(self) -> list[TaskModel]:
        with Session(self.engine) as session:
            tasks = list(session.execute(select(TaskModel)).scalars().all())
            return tasks

    def get_by_id(self, task_id: int) -> TaskModel | None:
        with Session(self.engine) as session:
            result = session.execute(
                select(TaskModel).where(TaskModel.id == task_id)
            )
            return result.scalar_one_or_none()

    def replace(self, task_id: int, task_dict: dict) -> TaskModel:
        with Session(self.engine) as session:
            result = session.execute(
                select(TaskModel).where(TaskModel.id == task_id)
            )
            replace_task = result.scalar_one_or_none()

            if not replace_task:
                raise ValueError(f"Задача с ID {task_id} не найдена")

            for key, value in task_dict.items():
                if hasattr(replace_task, key) and key != 'id':
                    setattr(replace_task, key, value)

            session.commit()
            session.refresh(replace_task)
            return replace_task

    def delete(self, task_id: int) -> bool:
        with Session(self.engine) as session:
            task_to_delete = session.get(TaskModel, task_id)

            if task_to_delete is None:
                return False

            session.delete(task_to_delete)
            session.commit()
            return True