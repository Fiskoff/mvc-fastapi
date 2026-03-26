from abc import ABC, abstractmethod
from typing import Optional, List, Dict, Any

from model import TaskModel
from view import TaskCreate, TaskResponse, TasksResponse, TaskUpdate


class InterfacesTaskRepository(ABC):

    @abstractmethod
    def create(self, task_dict: Dict[str, Any]) -> TaskModel:
        pass

    @abstractmethod
    def get_all(self) -> List[TaskModel]:
        pass

    @abstractmethod
    def get_by_id(self, task_id: int) -> Optional[TaskModel]:
        pass

    @abstractmethod
    def replace(self, task_id: int, task_dict: Dict[str, Any]) -> TaskModel:
        pass

    @abstractmethod
    def update(self, task_id: int, task_dict: Dict[str, Any]) -> Optional[TaskModel]:
        pass

    @abstractmethod
    def delete(self, task_id: int) -> bool:
        pass


class InterfacesTasksService(ABC):

    @abstractmethod
    def create_task(self, task: TaskCreate) -> TaskResponse:
        pass

    @abstractmethod
    def get_tasks(self) -> TasksResponse:
        pass

    @abstractmethod
    def get_task(self, task_id: int) -> Optional[TaskResponse]:
        pass

    @abstractmethod
    def replace_task(self, task_id: int, task_update: TaskUpdate) -> TaskResponse:
        pass

    @abstractmethod
    def change_task(self, task_id: int, task_update: TaskUpdate) -> Optional[TaskResponse]:
        pass

    @abstractmethod
    def delete_task(self, task_id: int) -> bool:
        pass