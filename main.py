import uvicorn
from fastapi import FastAPI
from sqlalchemy import create_engine

from task_model import BaseModel
from task_controller import router


engine = create_engine("sqlite+pysqlite:///:memory:", echo=True)

app = FastAPI()
app.include_router(router)

def create_tables():
    BaseModel.metadata.create_all(bind=engine)

def drop_tables():
    BaseModel.metadata.drop_all(bind=engine)


if __name__ == '__main__':
    create_tables()
    uvicorn.run("main:app", host="localhost", port=8000)







