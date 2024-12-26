from fastapi import APIRouter, Depends, status, Query
from sqlalchemy.ext.asyncio import AsyncSession

from src.core.database.dependencies import get_session
from src.core.database.repo import Repository

from src.group.models import UniversityGroup
from src.assignment.models import Assignment
from src.teacher.models import Teacher
from src.subject.models import Subject

from src.assignment.schemas import AssignmentCreateSchema, AssignmentSchema
from src.teacher.schemas import CreateTeacherSchema
from src.subject.schemas import CreateSubjectSchema
from src.group.schemas import GroupCreateSchema

from src.group.services.getter import GroupGetter
from src.teacher.services.getter import TeacherGetter
from src.subject.services.getter import SubjectGetter
from src.assignment.services.creator import AssignmentCreator

# from src.assignment.services.service import AssignmentService

router = APIRouter(prefix="/assignments", tags=["Assignments"])


@router.get("/", summary="Получить все занятия", response_model=list[AssignmentSchema])
async def get_all_assignments(
        group_name: str | None = Query(None, description="Название группы для фильтрации"),
        surname: str | None = Query(None, description="Фамилия преподавателя"),
        name: str | None = Query(None, description="Имя преподавателя"),
        patronym: str | None = Query(None, description="Отчество преподавателя"),
        session: AsyncSession = Depends(get_session)):
    repo = Repository[Assignment](Assignment, session)

    if group_name:
        group_getter = GroupGetter(Repository[UniversityGroup](UniversityGroup, session))
        group = await group_getter.get_by_name(group_name)
        group_filter = Assignment.group_id == group.id
    else:
        group_filter = None

    if surname and name and patronym:
        teacher_getter = TeacherGetter(Repository[Teacher](Teacher, session))
        teacher = await teacher_getter.get_by_full_name(surname, name, patronym)
        teacher_filter = Assignment.teacher_id = teacher.id
    else:
        teacher_filter = None

    filters = []
    if group_filter:
        filters.append(group_filter)
    if teacher_filter:
        filters.append(teacher_filter)

    assignments = await repo.get_all(filters=filters)

    # Проверять что препод и группа свободны во время занятия
    return assignments


@router.post("/", summary="Создать занятие", response_model=AssignmentSchema, status_code=status.HTTP_201_CREATED)
async def create_assignment(
        assignment_data: AssignmentCreateSchema,
        subject_data: CreateSubjectSchema,
        teacher_data: CreateTeacherSchema,
        group_data: GroupCreateSchema,
        session: AsyncSession = Depends(get_session)
):
    subject_getter = SubjectGetter(Repository[Subject](Subject, session))
    subject = await subject_getter.get_by_name(subject_data.subject_name)

    teacher_getter = TeacherGetter(Repository[Teacher](Teacher, session))
    teacher = await teacher_getter.get_by_full_name(teacher_data.surname, teacher_data.name, teacher_data.patronym)

    group_getter = GroupGetter(Repository[UniversityGroup](UniversityGroup, session))
    group = await group_getter.get_by_name(group_data.group_name)

    assignment_creator = AssignmentCreator(subject, teacher, group, Repository[Assignment](Assignment, session))
    created_assignment = await assignment_creator.create(assignment_data)

    return created_assignment
