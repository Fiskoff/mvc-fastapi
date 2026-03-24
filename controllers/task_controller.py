from typing import Annotated

from fastapi import APIRouter, Depends

from controllers.task_dependencies import get_tasks_service
from controllers.task_service import TasksService
from view import TaskResponse, TasksResponse, TaskCreate, TaskUpdate, DeleteTask


router = APIRouter()


@router.get("/tasks")
def get_tasks(service: Annotated[TasksService, Depends(get_tasks_service)]) -> TasksResponse:
    return service.get_tasks()


@router.get("/tasks/{task_id}")
def get_task(task_id: int, service: Annotated[TasksService, Depends(get_tasks_service)]) -> TaskResponse:
    return service.get_task(task_id)


@router.post("/tasks")
async def create_task(task: TaskCreate, service: Annotated[TasksService, Depends(get_tasks_service)]) -> TaskResponse:
    return service.create_task(task)


@router.put("/tasks/{task_id}")
async def replace_task(task_id: int, task: TaskUpdate, service: Annotated[TasksService, Depends(get_tasks_service)]) -> TaskResponse:
    return service.replace_task(task_id, task)


@router.patch("/tasks/{task_id}")
async def change_task(task_id: int, task: TaskUpdate, service: Annotated[TasksService, Depends(get_tasks_service)]) -> TaskResponse:
    return service.change_task(task_id, task)


@router.delete("/tasks/{task_id}")
async def delete_task(task_id: int, service: Annotated[TasksService, Depends(get_tasks_service)]):
    service.delete_task(task_id)
    return DeleteTask(id=task_id)
