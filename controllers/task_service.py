from sqlalchemy import Engine

from model import TaskModel, TaskRepository
from view import TaskResponse, GetTask, TasksResponse, TaskCreate, TaskUpdate


class TasksService:
    def __init__(self, engine: Engine) -> None:
        self.repo = TaskRepository(engine)

    @staticmethod
    def _to_response(task: TaskModel) -> TaskResponse:
        return TaskResponse(task=GetTask.model_validate(task))

    @staticmethod
    def _to_list_response(tasks: list[TaskModel]) -> TasksResponse:
        return TasksResponse(
            tasks=[GetTask.model_validate(t) for t in tasks],
            total=len(tasks),
            skip=0,
            limit=100,
        )

    def create_task(self, task: TaskCreate) -> TaskResponse:
        new_task = self.repo.create(task.model_dump())
        return self._to_response(new_task)

    def get_tasks(self) -> TasksResponse:
        tasks = self.repo.get_all()
        return TasksService._to_list_response(tasks)

    def get_task(self, task_id: int) -> TaskResponse | None:
        task = self.repo.get_by_id(task_id)
        return self._to_response(task) if task else None

    def replace_task(self, task_id: int, task_update: TaskUpdate) -> TaskResponse:
        updated = self.repo.replace(task_id, task_update.model_dump(exclude_unset=True))
        return self._to_response(updated)

    def change_task(self, task_id: int, task_update: TaskUpdate) -> TaskResponse | None:
        data = task_update.model_dump(exclude_unset=True)
        if not data:
            return None
        updated = self.repo.replace(task_id, data)
        return self._to_response(updated) if updated else None

    def delete_task(self, task_id: int) -> bool:
        return self.repo.delete(task_id)