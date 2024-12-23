from fastapi import APIRouter, Depends, status
from sqlalchemy.ext.asyncio import AsyncSession

from src.core.database.repo import Repository
from src.group.models import UniversityGroup
from src.group.services.getter import GroupGetter
from src.student.models import Student
from src.student.schemas import CreateStudentSchema, StudentSchema
from src.core.database.dependencies import get_session
from src.student.services.creator import StudentCreator
from src.user.models import User
from src.user.services.getter import UserGetter

router = APIRouter(prefix="/students", tags=["Students"])


@router.get("/", summary="Получить всех студентов", response_model=list[StudentSchema])
async def get_all_students(session: AsyncSession = Depends(get_session)):
    repo = Repository[Student](Student, session)
    students = await repo.get_all()
    return [StudentSchema.model_validate(student) for student in students]


@router.get("/{student_id}", summary="Получить данные конкретного студента", response_model=StudentSchema)
async def get_student_by_id(student_id: int, session: AsyncSession = Depends(get_session)):
    repo = Repository[Student](Student, session)
    student = await repo.get(id=student_id)
    return StudentSchema.model_validate(student)


@router.post("/", summary="Создать студента", response_model=StudentSchema, status_code=status.HTTP_201_CREATED)
async def create_student(
        student_data: CreateStudentSchema,
        user_login: str,
        session: AsyncSession = Depends(get_session)
):
    user_getter = UserGetter(Repository[User](User, session))
    user = await user_getter.get_by_login(user_login)

    group_getter = GroupGetter(Repository[UniversityGroup](UniversityGroup, session))
    group = await group_getter.get_by_id(student_data.group_id)

    student_creator = StudentCreator(user, group, Repository[Student](Student, session))
    created_student = await student_creator.create(student_data)
    return created_student
    # модель создается в момент входа через логин и пароль
    # Поверка, что юзер привязан именно к студенту?


@router.delete("/{student_id}", summary="Удалить студента", response_model=int)
async def delete_student(student_id: int, session: AsyncSession = Depends(get_session)):
    repo = Repository[Student](Student, session)
    await repo.delete(student_id)
    return student_id


@router.put("/{student_id}", summary="Обновить данные студента", response_model=StudentSchema)
async def update_student(
        student_id: int,
        student_data: CreateStudentSchema,
        session: AsyncSession = Depends(get_session)
):
    repo = Repository[Student](Student, session)
