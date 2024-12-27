from contextlib import asynccontextmanager

from fastapi import FastAPI, Request, HTTPException
from fastapi.middleware.cors import CORSMiddleware

from src.core.database.dependencies import get_session_manager

from authx.exceptions import MissingTokenError

from src.student.router import router as router_students
from src.user.router import router as router_users
from src.group.router import router as router_groups
from src.teacher.router import router as router_teachers
from src.subject.router import router as router_subjects
from src.admin.router import router as router_admins
from src.assignment.router import router as router_assignments
from src.auth.router import router as auth_router
from src.task.router import router as router_tasks
from src.report.router import router as router_reports


@asynccontextmanager
async def lifespan(app: FastAPI):
    yield

    session_manager = get_session_manager()
    await session_manager.close()


app = FastAPI(lifespan=lifespan, title='University System', debug=True)


@app.middleware('http')
async def auth(request: Request, call_next):
    try:
        response = await call_next(request)
        return response
    except MissingTokenError as e:
        raise HTTPException(status_code=401) from e


@app.get("/")
def home_page():
    return {"message": "Start page"}


# Настройка CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Разрешает запросы со всех источников
    allow_credentials=True,
    allow_methods=["*"],  # Разрешает все HTTP-методы
    allow_headers=["*"],  # Разрешает все заголовки
)

app.include_router(router_students)
app.include_router(router_users)
app.include_router(router_groups)
app.include_router(router_teachers)
app.include_router(router_subjects)
app.include_router(router_admins)
app.include_router(router_assignments)
app.include_router(router_tasks)
app.include_router(router_reports)
app.include_router(auth_router)
