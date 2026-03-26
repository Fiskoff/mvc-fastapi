from typing import Annotated

from fastapi import Depends

from model import TaskRepository
from controllers.task_service import TasksService
from config import engine


def get_repository() -> TaskRepository:
    return TaskRepository(engine)


def get_tasks_service(repo: Annotated[TaskRepository, Depends(get_repository)]) -> TasksService:
    return TasksService(repo)