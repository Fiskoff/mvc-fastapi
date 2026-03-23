from fastapi import APIRouter
from sqlalchemy import Engine

from task_model import TaskModel, TaskRepository
from task_view import TaskResponse, TasksResponse, TaskCreate, TaskUpdate, GetTask

router = APIRouter()


@router.get("/tasks")
def get_tasks() -> TasksResponse:
    return TasksService.get_tasks()

@router.get("/tasks/{task_id}")
def get_task(task_id: int) -> TaskResponse:
    return TasksService.get_task(task_id)

@router.post("/tasks")
async def create_task(task: TaskCreate) -> TaskResponse:
    return TasksService.create_task(task)

@router.put("/tasks/{task_id}")
async def replace_task(task_id: int, task: TaskUpdate) -> TaskResponse:
    return TasksService.replace_task(task_id, task)

@router.patch("/tasks/{task_id}")
async def change_task(task_id: int, task: TaskUpdate) -> TaskResponse:
    return TasksService.change_task(task_id, task)

@router.delete("/tasks/{task_id}")
async def delete_task(task_id: int):
    TasksService.delete_task(task_id)


class TasksService:
    def __init__(self, engine: Engine) -> None:
        self.repo = TaskRepository(engine)

    @staticmethod
    def _to_response(task: TaskModel) -> TaskResponse:
        return TaskResponse(task=GetTask.model_validate(task))

    def create_task(self, task: TaskCreate) -> TaskResponse:
        task_dict = task.model_dump()
        new_task = self.repo.create(task_dict)
        return self._to_response(new_task)

    def get_tasks(self) -> TasksResponse:
        tasks = self.repo.get_all()
        return self._to_response(tasks)

    def get_task(self, task_id: int) -> TaskResponse | None:
        task = self.repo.get_by_id(task_id)
        if task is None:
            return None
        return self._to_response(task)

    def replace_task(self, task_id: int, task_update: TaskUpdate) -> TaskResponse:
        task_dict = task_update.model_dump(exclude_unset=True)
        updated = self.repo.replace(task_id, task_dict)
        return self._to_response(updated)

    def change_task(self, task_id: int, task_update: TaskUpdate) -> TaskResponse | None:
        task_dict = task_update.model_dump(exclude_unset=True)
        if not task_dict:
            return None
        updated = self.repo.replace(task_id, task_dict)
        if updated is None:
            return None
        return self._to_response(updated)

    def delete_task(self, task_id: int) -> bool:
        return self.repo.delete(task_id)