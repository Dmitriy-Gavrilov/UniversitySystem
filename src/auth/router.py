from fastapi import APIRouter, Response, Depends, HTTPException
from authx import AuthX, AuthXConfig

from src.auth.exceptions import OtherRoleRequired
from src.auth.schemas import AuthSchema, AuthResponseSchema
from src.core.database.repo import Repository
from src.settings import SECRET_KEY, JWT_ACCESS_COOKIE_NAME
from src.user.exceptions import UserNotFoundError, WrongUserPassword
from src.user.models import User
from src.user.services.getter import UserGetter
from sqlalchemy.ext.asyncio import AsyncSession
from src.core.database.dependencies import get_session

router = APIRouter(prefix='/auth', tags=['Auth'])


config = AuthXConfig(
    JWT_ALGORITHM='HS256',
    JWT_SECRET_KEY=SECRET_KEY,
    JWT_ACCESS_COOKIE_NAME=JWT_ACCESS_COOKIE_NAME,
    JWT_TOKEN_LOCATION=['cookies'],
)

security = AuthX(config=config)


@router.post('/login', response_model=AuthResponseSchema, summary='Вход')
async def login(
        auth: AuthSchema,
        response: Response,
        session: AsyncSession = Depends(get_session)
) -> AuthResponseSchema:

    user_getter = UserGetter(Repository[User](User, session))
    try:
        user = await user_getter.get_for_login(auth.login, auth.password)
        if user.role != auth.role:
            raise OtherRoleRequired()

        token = security.create_access_token(uid=str(user.id))
        response.set_cookie(config.JWT_ACCESS_COOKIE_NAME, token, httponly=True)
        return AuthResponseSchema(access_token=token)
    except (UserNotFoundError, OtherRoleRequired, WrongUserPassword):
        raise HTTPException(401, detail={'message': 'Wrong auth data'})
