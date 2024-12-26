from fastapi import APIRouter, Depends, status, Query
from sqlalchemy import inspect
from sqlalchemy.ext.asyncio import AsyncSession

from src.core.database.repo import Repository
from src.core.database.dependencies import get_session

from src.group.models import UniversityGroup
from src.group.services.getter import GroupGetter

from src.student.models import Student
from src.student.schemas import CreateStudentSchema, StudentSchema, ResponseStudentSchema
from src.student.services.creator import StudentCreator
from src.student.services.service import StudentService

from src.user.models import User
from src.user.schemas import CreateUserSchema
from src.user.services.getter import UserGetter

router = APIRouter(prefix="/students", tags=["Students"])


# @router.get("/", summary="Получить всех студентов", response_model=list[StudentSchema])
# async def get_all_students(
#         group_name: str | None = Query(None, description="Название группы для фильтрации"),
#         session: AsyncSession = Depends(get_session)):
#     repo = Repository[Student](Student, session)
#
#     if group_name:
#         group_getter = GroupGetter(Repository[UniversityGroup](UniversityGroup, session))
#         group = await group_getter.get_by_name(group_name)
#         students = await repo.get_all(filters=[Student.group_id == group.id])
#     else:
#         students = await repo.get_all()
#     return [StudentSchema.model_validate(student) for student in students]

@router.get("/", summary="Получить всех студентов", response_model=list[ResponseStudentSchema])
async def get_all_students(
        group_name: str | None = Query(None, description="Название группы для фильтрации"),
        session: AsyncSession = Depends(get_session)):
    repo = Repository[Student](Student, session)

    if group_name:
        group_getter = GroupGetter(Repository[UniversityGroup](UniversityGroup, session))
        group = await group_getter.get_by_name(group_name)
        students = await repo.get_all(filters=[Student.group_id == group.id])
    else:
        students = await repo.get_all()

    group_ids = {student.group_id for student in students}
    group_repo = Repository[UniversityGroup](UniversityGroup, session)
    groups = await group_repo.get_all(filters=[UniversityGroup.id.in_(group_ids)])
    group_map = {group.id: group.group_name for group in groups}

    def student_to_dict(student):
        student_dict = {column.key: getattr(student, column.key) for column in inspect(student).mapper.column_attrs}
        student_dict["group_name"] = group_map.get(student.group_id, "Unknown")
        return student_dict

    return [ResponseStudentSchema.model_validate(student_to_dict(student)) for student in students]


@router.get("/{student_id}", summary="Получить данные студента по ID", response_model=StudentSchema)
async def get_student_by_id(student_id: int, session: AsyncSession = Depends(get_session)):
    student_service = StudentService(Repository[Student](Student, session))
    return await student_service.get_by_id(student_id)


@router.post("/", summary="Создать студента", response_model=StudentSchema, status_code=status.HTTP_201_CREATED)
async def create_student(
        student_data: CreateStudentSchema,
        user_data: CreateUserSchema,
        session: AsyncSession = Depends(get_session)
):
    user_getter = UserGetter(Repository[User](User, session))
    user = await user_getter.get_for_login(user_data.login, user_data.password)

    group_getter = GroupGetter(Repository[UniversityGroup](UniversityGroup, session))
    group = await group_getter.get_by_id(student_data.group_id)

    student_creator = StudentCreator(user, group, Repository[Student](Student, session))
    created_student = await student_creator.create(student_data)

    return created_student
    # модель создается в момент входа через логин и пароль
    # Проверка, что юзер привязан именно к студенту?


@router.delete("/{student_id}", summary="Удалить студента", response_model=int)
async def delete_student(student_id: int, session: AsyncSession = Depends(get_session)):
    student_service = StudentService(Repository[Student](Student, session))
    await student_service.delete(student_id)
    return student_id


@router.put("/{student_id}", summary="Обновить данные студента", response_model=StudentSchema)
async def update_student(
        student_id: int,
        student_data: CreateStudentSchema,
        session: AsyncSession = Depends(get_session)
):
    student_service = StudentService(Repository[Student](Student, session))
    return await student_service.update(student_id, student_data)
