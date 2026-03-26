from pydantic import BaseModel, Field, ConfigDict


class TaskBase(BaseModel):
    title: str = Field(min_length=1, max_length=100, examples=["Тестовое задание"])
    description: str | None = Field(None, examples=["Текст описывающий задачу"])
    is_completed: bool = Field(False, examples=[False])


class TaskCreate(TaskBase):
    pass


class TaskUpdate(BaseModel):
    title: str | None = Field(None, min_length=1, max_length=100, examples=["Обновленное название задачи"])
    description: str | None = Field(None, examples=["Обновленное описание"])
    is_completed: bool | None = Field(None, examples=[True])


class GetTask(BaseModel):
    id: int = Field(examples=[1])
    title: str = Field(min_length=1, max_length=100, examples=["Завершить тестовое задание"])
    description: str | None = Field(None, examples=["Текст описывающий задачу"])
    is_completed: bool = Field(False, examples=[False])
    model_config = ConfigDict(from_attributes=True)


class TaskResponse(BaseModel):
    task: GetTask


class TasksResponse(BaseModel):
    tasks: list[GetTask]


class DeleteTask(BaseModel):
    message: str = "success"
    id: int = Field(examples=[1])