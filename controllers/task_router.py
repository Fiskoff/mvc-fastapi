from typing import Annotated

from fastapi import APIRouter, Depends, HTTPException

from controllers.task_dependencies import get_tasks_service
from controllers.task_service import TasksService
from view import TaskResponse, TasksResponse, TaskCreate, TaskUpdate, DeleteTask


router = APIRouter()


@router.get("/tasks")
def get_tasks(service: Annotated[TasksService, Depends(get_tasks_service)]) -> TasksResponse:
    return service.get_tasks()


@router.get("/tasks/{task_id}")
def get_task(task_id: int, service: Annotated[TasksService, Depends(get_tasks_service)]) -> TaskResponse:
    task = service.get_task(task_id)
    if task is None:
        raise HTTPException(status_code=404, detail=f"Task with id {task_id} not found")
    return task


@router.post("/tasks")
async def create_task(task: TaskCreate, service: Annotated[TasksService, Depends(get_tasks_service)]) -> TaskResponse:
    return service.create_task(task)


@router.put("/tasks/{task_id}")
async def replace_task(task_id: int, task: TaskUpdate, service: Annotated[TasksService, Depends(get_tasks_service)]) -> TaskResponse:
    try:
        return service.replace_task(task_id, task)
    except ValueError:
        raise HTTPException(status_code=404, detail=f"Task with id {task_id} not found")


@router.patch("/tasks/{task_id}")
async def change_task(task_id: int, task: TaskUpdate, service: Annotated[TasksService, Depends(get_tasks_service)]) -> TaskResponse:
    result = service.change_task(task_id, task)
    if result is None:
        raise HTTPException(status_code=404, detail=f"Task with id {task_id} not found")
    return result


@router.delete("/tasks/{task_id}")
async def delete_task(task_id: int, service: Annotated[TasksService, Depends(get_tasks_service)]):
    deleted = service.delete_task(task_id)
    if not deleted:
        raise HTTPException(status_code=404, detail=f"Task with id {task_id} not found")
    return DeleteTask(id=task_id)