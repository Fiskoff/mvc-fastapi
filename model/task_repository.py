from sqlalchemy import Engine, select
from sqlalchemy.orm import Session
from typing import Optional, List, Dict, Any

from model import TaskModel


class TaskRepository:
    def __init__(self, engine: Engine) -> None:
        self.engine = engine

    def create(self, task_dict: Dict[str, Any]) -> TaskModel:
        new_task = TaskModel(**task_dict)
        with Session(self.engine) as session:
            session.add(new_task)
            session.commit()
            session.refresh(new_task)
            return new_task

    def get_all(self) -> List[TaskModel]:
        with Session(self.engine) as session:
            result = session.execute(select(TaskModel)).scalars()
            return list(result.all())

    def get_by_id(self, task_id: int) -> Optional[TaskModel]:
        with Session(self.engine) as session:
            result = session.execute(
                select(TaskModel).where(TaskModel.id == task_id)
            )
            return result.scalar_one_or_none()

    def replace(self, task_id: int, task_dict: Dict[str, Any]) -> TaskModel:
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

    def update(self, task_id: int, task_dict: Dict[str, Any]) -> Optional[TaskModel]:
        with Session(self.engine) as session:
            result = session.execute(
                select(TaskModel).where(TaskModel.id == task_id)
            )
            update_task = result.scalar_one_or_none()

            if not update_task:
                return None

            for key, value in task_dict.items():
                if hasattr(update_task, key) and key != 'id':
                    setattr(update_task, key, value)

            session.commit()
            session.refresh(update_task)
            return update_task

    def delete(self, task_id: int) -> bool:
        with Session(self.engine) as session:
            task_to_delete = session.get(TaskModel, task_id)

            if task_to_delete is None:
                return False

            session.delete(task_to_delete)
            session.commit()
            return True