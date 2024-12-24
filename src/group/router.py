from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession

from src.core.database.dependencies import get_session
from src.core.database.repo import Repository
from src.group.schemas import GroupCreateSchema, GroupSchema
from src.group.models import UniversityGroup
from src.group.services.service import GroupService

router = APIRouter(prefix="/groups", tags=["Groups"])


@router.get("/{group_id}", summary="Получить группу по ID", response_model=GroupSchema)
async def get_user_by_id(
        group_id: int,
        session: AsyncSession = Depends(get_session)):
    group_service = GroupService(Repository[UniversityGroup](UniversityGroup, session))
    return await group_service.get_by_id(group_id)


@router.post("/", summary="Создать группу", response_model=GroupSchema, status_code=status.HTTP_201_CREATED)
async def create_group(
        group_data: GroupCreateSchema,
        session: AsyncSession = Depends(get_session)):
    group_service = GroupService(Repository[UniversityGroup](UniversityGroup, session))
    return await group_service.create(group_data)


@router.delete("/", summary="Удалить группу", status_code=status.HTTP_204_NO_CONTENT)
async def delete_group(
        group_id: int,
        session: AsyncSession = Depends(get_session)):
    group_service = GroupService(Repository[UniversityGroup](UniversityGroup, session))
    return group_service.delete(group_id)
