from sqlalchemy import create_engine

DATABASE_URL = "sqlite:///example.db"

engine = create_engine(DATABASE_URL, echo=True)
from model import BaseModel
from model.engine import engine, DATABASE_URL


def create_tables():
    BaseModel.metadata.create_all(bind=engine)