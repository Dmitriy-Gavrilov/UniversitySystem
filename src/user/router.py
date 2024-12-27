from fastapi import APIRouter, Depends, status, Request
from sqlalchemy.ext.asyncio import AsyncSession

from src.auth.role_validator import AuthRoleVerifier
from src.auth.router import security
from src.auth.utils import get_user
from src.core.database.dependencies import get_session
from src.core.database.repo import Repository
from src.user.schemas import CreateUserSchema, UserSchema
from src.user.models import User, UserRole
from src.user.services.service import UserService

router = APIRouter(prefix="/users", tags=["Users"])


@router.get(
    path="/{user_id}",
    summary="Получить пользователя по ID",
    response_model=UserSchema,
    dependencies=[Depends(security.access_token_required)],
)
async def get_user_by_id(
        request: Request,
        user_id: int,
        session: AsyncSession = Depends(get_session)
):
    user = await get_user(request, session)
    AuthRoleVerifier(user).verify(required_role=UserRole.ADMIN)

    user_service = UserService(Repository[User](User, session))
    return await user_service.get_by_id(user_id)


@router.post(
    path="/",
    summary="Создать пользователя",
    response_model=UserSchema,
    status_code=status.HTTP_201_CREATED,
    dependencies=[Depends(security.access_token_required)],
)
async def create_user(
        request: Request,
        user_data: CreateUserSchema,
        session: AsyncSession = Depends(get_session)
):
    user = await get_user(request, session)
    AuthRoleVerifier(user).verify(required_role=UserRole.ADMIN)

    user_creator = UserService(Repository[User](User, session))
    return await user_creator.create(user_data)


@router.delete(
    path="/",
    summary="Удалить пользователя",
    response_model=int,
    dependencies=[Depends(security.access_token_required)],
)
async def delete_user(
        request: Request,
        user_id: int,
        session: AsyncSession = Depends(get_session),
):
    user = await get_user(request, session)
    AuthRoleVerifier(user).verify(required_role=UserRole.ADMIN)

    user_service = UserService(Repository[User](User, session))
    await user_service.delete(user_id)
    return user_id

