from sqlalchemy import create_engine
from model import BaseModel


DATABASE_URL = "sqlite:///example.db"
engine = create_engine(DATABASE_URL, echo=True)

def create_tables():
    BaseModel.metadata.create_all(bind=engine)