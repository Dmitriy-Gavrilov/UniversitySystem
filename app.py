from contextlib import asynccontextmanager

import uvicorn
from fastapi import FastAPI

from src.core.database.dependencies import get_session_manager

from src.student.router import router as router_students
from src.user.router import router as router_users
from src.group.router import router as router_groups


@asynccontextmanager
async def lifespan(app: FastAPI):
    yield

    session_manager = get_session_manager()
    await session_manager.close()


app = FastAPI(lifespan=lifespan, title='University System', debug=True)


@app.get("/")
def home_page():
    return {"message": "Start page"}


app.include_router(router_students)
app.include_router(router_users)
app.include_router(router_groups)
