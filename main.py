import uvicorn
from fastapi import FastAPI

from controllers.task_router import router
from config import create_tables


def main():
    create_tables()

    app = FastAPI()
    app.include_router(router)

    uvicorn.run(app, host="localhost", port=8000)


if __name__ == '__main__':
    main()