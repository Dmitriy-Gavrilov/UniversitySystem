from fastapi import APIRouter, Depends, status
from sqlalchemy.ext.asyncio import AsyncSession

from src.core.database.repo import Repository
from src.core.database.dependencies import get_session

from src.admin.models import Administrator
from src.admin.schemas import AdminCreateSchema, AdminSchema
from src.admin.services.creator import AdminCreator
from src.admin.services.service import AdminService
from src.user.models import User
from src.user.schemas import CreateUserSchema
from src.user.services.getter import UserGetter

router = APIRouter(prefix="/admins", tags=["Administrators"])


@router.get("/{admin_id}", summary="Получить данные администратора по ID", response_model=AdminSchema)
async def get_admin_by_id(admin_id: int, session: AsyncSession = Depends(get_session)):
    admin_service = AdminService(Repository[Administrator](Administrator, session))
    return await admin_service.get_by_id(admin_id)


@router.post("/", summary="Создать администратора", response_model=AdminSchema, status_code=status.HTTP_201_CREATED)
async def create_admin(
        admin_data: AdminCreateSchema,
        user_data: CreateUserSchema,
        session: AsyncSession = Depends(get_session)
):
    user_getter = UserGetter(Repository[User](User, session))
    user = await user_getter.get_for_login(user_data.login, user_data.password)

    admin_creator = AdminCreator(user, Repository[Administrator](Administrator, session))
    created_admin = await admin_creator.create(admin_data)

    return created_admin


@router.put("/{admin_id}", summary="Обновить данные администратора", response_model=AdminSchema)
async def update_admin(
        admin_id: int,
        admin_data: AdminCreateSchema,
        session: AsyncSession = Depends(get_session)
):
    admin_service = AdminService(Repository[Administrator](Administrator, session))
    return await admin_service.update(admin_id, admin_data)


@router.delete("/{admin_id}", summary="Удалить администратора", response_model=int)
async def delete_admin(
        admin_id: int,
        session: AsyncSession = Depends(get_session)):
    admin_service = AdminService(Repository[Administrator](Administrator, session))
    await admin_service.delete(admin_id)
    return admin_id

