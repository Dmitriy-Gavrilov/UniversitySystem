from sqlalchemy.ext.asyncio import AsyncSession

from src.core.database.session_manager import SessionManager
from src.settings import DATABASE_URL

def get_session_manager() -> SessionManager:
    return SessionManager(DATABASE_URL, {'echo': True})


async def get_session() -> AsyncSession:
    session_manager = get_session_manager()
    async with session_manager.session() as session:
        yield session