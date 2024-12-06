from sqlalchemy.ext.asyncio import AsyncSession

from src.core.database.session_manager import SessionManager
from src.settings import DATABASE_URL


async def get_session() -> AsyncSession:
    sessionmanager = SessionManager(DATABASE_URL, {'echo': True})
    async with sessionmanager.session() as session:
        yield session