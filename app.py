from contextlib import asynccontextmanager

import uvicorn
from fastapi import FastAPI

from src.core.database.dependencies import get_session_manager


@asynccontextmanager
async def lifespan(app: FastAPI):
    yield

    session_manager = get_session_manager()
    await session_manager.close()


app = FastAPI(lifespan=lifespan, title='University System', debug=True)

