from typing import Annotated

from fastapi import Depends
from sqlalchemy import Engine
from sqlalchemy.orm import Session

from model.task_repository import TaskRepository
from controllers.task_service import TasksService

def get_db_session(engine: Engine) -> Session:
    with Session(engine) as session:
        yield session


def get_repository(session: Annotated[Session, Depends(get_db_session)]) -> TaskRepository:
    return TaskRepository(session)


def get_tasks_service(repo: Annotated[TaskRepository, Depends(get_repository)]) -> "TasksService":
    return TasksService(repo)
