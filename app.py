from contextlib import asynccontextmanager

import uvicorn
from fastapi import FastAPI

from src.core.database.dependencies import get_session_manager

from src.student.router import router as router_students
from src.user.router import router as router_users
from src.group.router import router as router_groups
from src.teacher.router import router as router_teachers
from src.subject.router import router as router_subjects
from src.admin.router import router as router_admins
from src.assignment.router import router as router_assignments
from src.task.router import router as router_tasks


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
app.include_router(router_teachers)
app.include_router(router_subjects)
app.include_router(router_admins)
app.include_router(router_assignments)
app.include_router(router_tasks)
