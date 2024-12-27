from fastapi import Request
from authx import RequestToken, TokenPayload
from sqlalchemy.ext.asyncio import AsyncSession

from src.auth.router import security
from src.core.database.repo import Repository
from src.user.models import User


async def validate_token_from_request(request: Request) -> TokenPayload:
    token: RequestToken = await security.get_access_token_from_request(request)
    token_payload: TokenPayload = security.verify_token(token, verify_csrf=False)
    return token_payload


async def get_user_from_token_payload(token_payload: TokenPayload, session: AsyncSession) -> User:
    user_id = int(token_payload.sub)
    repo = Repository[User](User, session)
    return await repo.get(id=user_id)


async def get_user(request: Request, session: AsyncSession) -> User:
    token_payload = await validate_token_from_request(request)
    user = await get_user_from_token_payload(token_payload, session)
    return user
