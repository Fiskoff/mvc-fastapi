from typing import Annotated

from fastapi import Depends

from interfaces import InterfacesTaskRepository, InterfacesTasksService
from model import TaskRepository
from controllers.task_service import TasksService
from config import engine


def get_repository() -> InterfacesTaskRepository:
    return TaskRepository(engine)


def get_tasks_service(repo: Annotated[InterfacesTaskRepository, Depends(get_repository)]) -> InterfacesTasksService:
    return TasksService(repo)