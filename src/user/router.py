from fastapi import APIRouter, Depends, status
from sqlalchemy.ext.asyncio import AsyncSession

from src.core.database.dependencies import get_session
from src.core.database.repo import Repository
from src.user.schemas import CreateUserSchema, UserSchema
from src.user.models import User
from src.user.services.service import UserService

router = APIRouter(prefix="/users", tags=["Users"])


@router.get("/{user_id}", summary="Получить пользователя по ID", response_model=UserSchema)
async def get_user_by_id(
        user_id: int,
        session: AsyncSession = Depends(get_session)):
    user_service = UserService(Repository[User](User, session))
    return await user_service.get_by_id(user_id)


@router.post("/", summary="Создать пользователя", response_model=UserSchema, status_code=status.HTTP_201_CREATED)
async def create_user(
        user_data: CreateUserSchema,
        session: AsyncSession = Depends(get_session)):
    user_creator = UserService(Repository[User](User, session))
    return await user_creator.create(user_data)


@router.delete("/", summary="Удалить пользователя", response_model=int)
async def delete_user(
        user_id: int,
        session: AsyncSession = Depends(get_session)):
    user_service = UserService(Repository[User](User, session))
    await user_service.delete(user_id)
    return user_id

