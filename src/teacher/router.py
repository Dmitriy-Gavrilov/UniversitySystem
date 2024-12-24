from fastapi import APIRouter, Depends, status
from sqlalchemy.ext.asyncio import AsyncSession

from src.core.database.repo import Repository
from src.core.database.dependencies import get_session

from src.teacher.models import Teacher
from src.teacher.schemas import CreateTeacherSchema, TeacherSchema
from src.teacher.services.creator import TeacherCreator
from src.teacher.services.service import TeacherService
from src.user.models import User
from src.user.schemas import CreateUserSchema
from src.user.services.getter import UserGetter

router = APIRouter(prefix="/teachers", tags=["Teachers"])


@router.get("/", summary="Получить всех преподавателей", response_model=list[TeacherSchema])
async def get_all_teachers(session: AsyncSession = Depends(get_session)):
    repo = Repository[Teacher](Teacher, session)
    teachers = await repo.get_all()
    return [TeacherSchema.model_validate(student) for student in teachers]


@router.get("/{teacher_id}", summary="Получить данные преподавателя по ID", response_model=TeacherSchema)
async def get_teacher_by_id(teacher_id: int, session: AsyncSession = Depends(get_session)):
    teacher_service = TeacherService(Repository[Teacher](Teacher, session))
    return await teacher_service.get_by_id(teacher_id)


@router.post("/", summary="Создать преподавателя", response_model=TeacherSchema, status_code=status.HTTP_201_CREATED)
async def create_student(
        teacher_data: CreateTeacherSchema,
        user_data: CreateUserSchema,
        session: AsyncSession = Depends(get_session)
):
    user_getter = UserGetter(Repository[User](User, session))
    user = await user_getter.get_for_login(user_data.login, user_data.password)

    teacher_creator = TeacherCreator(user, Repository[Teacher](Teacher, session))
    created_teacher = await teacher_creator.create(teacher_data)

    return created_teacher


@router.put("/{teacher_id}", summary="Обновить данные преподавателя", response_model=TeacherSchema)
async def update_student(
        teacher_id: int,
        teacher_data: CreateTeacherSchema,
        session: AsyncSession = Depends(get_session)
):
    teacher_service = TeacherService(Repository[Teacher](Teacher, session))
    return await teacher_service.update(teacher_id, teacher_data)


@router.delete("/{teacher_id}", summary="Удалить преподавателя", response_model=int)
async def delete_student(
        teacher_id: int,
        session: AsyncSession = Depends(get_session)):
    teacher_service = TeacherService(Repository[Teacher](Teacher, session))
    await teacher_service.delete(teacher_id)
    return teacher_id
