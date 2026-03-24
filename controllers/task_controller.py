from fastapi import APIRouter

from controllers.task_service import TasksService
from view import TaskResponse, TasksResponse, TaskCreate, TaskUpdate


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
