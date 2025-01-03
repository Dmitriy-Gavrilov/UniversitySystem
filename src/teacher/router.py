from fastapi import APIRouter, Depends, status, Request
from sqlalchemy.ext.asyncio import AsyncSession

from src.assignment.models import Assignment
from src.auth.role_validator import AuthRoleVerifier
from src.auth.router import security
from src.auth.utils import get_user
from src.core.database.repo import Repository
from src.core.database.dependencies import get_session
from src.subject.models import Subject

from src.teacher.models import Teacher
from src.teacher.schemas import CreateTeacherSchema, TeacherSchema, ResponseTeacherSchema
from src.teacher.services.creator import TeacherCreator
from src.teacher.services.service import TeacherService
from src.user.models import UserRole

router = APIRouter(prefix="/teachers", tags=["Teachers"])


@router.get(
    path="/",
    summary="Получить всех преподавателей",
    response_model=list[TeacherSchema],
    dependencies=[Depends(security.access_token_required)],
)
async def get_all_teachers(request: Request, session: AsyncSession = Depends(get_session)):
    user = await get_user(request, session)
    AuthRoleVerifier(user).verify(required_role=UserRole.TEACHER)

    repo = Repository[Teacher](Teacher, session)
    teachers = await repo.get_all()
    return [TeacherSchema.model_validate(student) for student in teachers]


@router.get(
    path="/{teacher_id}",
    summary="Получить данные преподавателя по ID",
    response_model=TeacherSchema,
    dependencies=[Depends(security.access_token_required)],
)
async def get_teacher_by_id(request: Request, teacher_id: int, session: AsyncSession = Depends(get_session)):
    user = await get_user(request, session)
    AuthRoleVerifier(user).verify(required_role=UserRole.TEACHER)

    teacher_service = TeacherService(Repository[Teacher](Teacher, session))
    return await teacher_service.get_by_id(teacher_id)


@router.get(
    path="/full_info/{teacher_id}",
    summary="Получить данные преподавателя вместе с предметами",
    response_model=ResponseTeacherSchema,
    dependencies=[Depends(security.access_token_required)],
)
async def get_full_info_teacher_by_id(request: Request, teacher_id: int, session: AsyncSession = Depends(get_session)):
    user = await get_user(request, session)
    AuthRoleVerifier(user).verify(required_role=UserRole.TEACHER)

    teacher_service = TeacherService(Repository[Teacher](Teacher, session))
    return await teacher_service.get_full_info(
        teacher_id,
        Repository[Assignment](Assignment, session),
        Repository[Subject](Subject, session)
    )


@router.post(
    path="/",
    summary="Создать преподавателя",
    response_model=TeacherSchema,
    status_code=status.HTTP_201_CREATED,
    dependencies=[Depends(security.access_token_required)],
)
async def create_teacher(
        teacher_data: CreateTeacherSchema,
        request: Request,
        session: AsyncSession = Depends(get_session)
):
    user = await get_user(request, session)
    AuthRoleVerifier(user).verify(required_role=UserRole.ADMIN)

    teacher_creator = TeacherCreator(user, Repository[Teacher](Teacher, session))
    created_teacher = await teacher_creator.create(teacher_data)

    return created_teacher


@router.put(
    path="/{teacher_id}",
    summary="Обновить данные преподавателя",
    response_model=TeacherSchema,
    dependencies=[Depends(security.access_token_required)],
)
async def update_teacher(
        teacher_id: int,
        request: Request,
        teacher_data: CreateTeacherSchema,
        session: AsyncSession = Depends(get_session)
):
    user = await get_user(request, session)
    AuthRoleVerifier(user).verify(required_role=UserRole.TEACHER)

    teacher_service = TeacherService(Repository[Teacher](Teacher, session))
    return await teacher_service.update(teacher_id, teacher_data)


@router.delete(
    path="/{teacher_id}",
    summary="Удалить преподавателя",
    response_model=int,
    dependencies=[Depends(security.access_token_required)],
)
async def delete_teacher(
        request: Request,
        teacher_id: int,
        session: AsyncSession = Depends(get_session)
):
    user = await get_user(request, session)
    AuthRoleVerifier(user).verify(required_role=UserRole.ADMIN)

    teacher_service = TeacherService(Repository[Teacher](Teacher, session))
    await teacher_service.delete(teacher_id)
    return teacher_id
