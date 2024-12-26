from fastapi import APIRouter, Depends, status, Query
from sqlalchemy.ext.asyncio import AsyncSession

from src.assignment.services.getter import AssignmentGetter
from src.core.database.dependencies import get_session
from src.core.database.repo import Repository

from src.group.models import UniversityGroup
from src.assignment.models import Assignment
from src.task.services.creator import TaskCreator
from src.teacher.models import Teacher
from src.subject.models import Subject
from src.task.models import Task

from src.task.schemas import TaskSchema, CreateTaskSchema, ResponseTaskSchema

from src.group.services.getter import GroupGetter
from src.teacher.services.getter import TeacherGetter
from src.subject.services.getter import SubjectGetter

router = APIRouter(prefix="/tasks", tags=["Tasks"])


@router.get("/", summary="Получить все задания", response_model=list[ResponseTaskSchema])
async def get_all_tasks(
        group_name: str | None = Query(None, description="Название группы для фильтрации"),
        surname: str | None = Query(None, description="Фамилия преподавателя"),
        name: str | None = Query(None, description="Имя преподавателя"),
        patronym: str | None = Query(None, description="Отчество преподавателя"),
        subject_name: str | None = Query(None, description="Название предмета"),
        session: AsyncSession = Depends(get_session)):
    repo_task = Repository[Task](Task, session)
    repo_assignment = Repository[Assignment](Assignment, session)
    repo_subject = Repository[Subject](Subject, session)
    repo_teacher = Repository[Teacher](Teacher, session)
    repo_group = Repository[UniversityGroup](UniversityGroup, session)

    tasks = []
    if any([group_name, surname, name, patronym, subject_name]):
        assignment_getter = AssignmentGetter(Repository[Assignment](Assignment, session))
        if group_name:
            group_getter = GroupGetter(Repository[UniversityGroup](UniversityGroup, session))
            group = await group_getter.get_by_name(group_name)
            print(group.group_name, group.id)
            assignments = await assignment_getter.get_by_parameters([UniversityGroup.group_name == group.group_name])
            print("len===", len(assignments))
            for i in assignments:
                tasks.append(*await repo_task.get_all(Task.assignment_id == i.id))

        # if surname and name and patronym:
        #     teacher_getter = TeacherGetter(Repository[Teacher](Teacher, session))
        #     teacher = await teacher_getter.get_by_full_name(surname, name, patronym)
        #     assignments = await assignment_getter.get_by_parameters([Teacher.id == teacher.id])
        #     for i in assignments:
        #         if i not in tasks:
        #             tasks.append(*await repo_task.get_all(Task.assignment_id == i.id))
        #
        # if subject_name:
        #     subject_getter = SubjectGetter(Repository[Subject](Subject, session))
        #     subject = await subject_getter.get_by_name(subject_name)
        #     assignments = await assignment_getter.get_by_parameters([Subject.id == subject.id])
        #     for i in assignments:
        #         tasks.append(*await repo_task.get_all(Task.assignment_id == i.id))
    else:
        tasks = await repo_task.get_all()

    response = []

    for task in tasks:
        assignment = await repo_assignment.get(id=task.assignment_id)
        subject = await repo_subject.get(id=assignment.subject_id)
        teacher = await repo_teacher.get(id=assignment.teacher_id)
        group = await repo_group.get(id=assignment.group_id)

        response.append(ResponseTaskSchema(
            **task.__dict__,
            subject_name=subject.subject_name,
            teacher_surname=teacher.surname,
            teacher_name=teacher.name,
            teacher_patronym=teacher.patronym,
            group_name=group.group_name))

    return response


@router.post("/", summary="Создать задание", response_model=TaskSchema, status_code=status.HTTP_201_CREATED)
async def create_task(
        task_name: str,
        points: int,
        group_name: str,
        subject_name: str,
        surname: str,
        name: str,
        patronym: str,
        session: AsyncSession = Depends(get_session)
):
    repo_assignment = Repository[Assignment](Assignment, session)

    group_getter = GroupGetter(Repository[UniversityGroup](UniversityGroup, session))
    group = await group_getter.get_by_name(group_name)

    teacher_getter = TeacherGetter(Repository[Teacher](Teacher, session))
    teacher = await teacher_getter.get_by_full_name(surname, name, patronym)

    subject_getter = SubjectGetter(Repository[Subject](Subject, session))
    subject = await subject_getter.get_by_name(subject_name)

    assignment = await repo_assignment.get(group_id=group.id, teacher_id=teacher.id, subject_id=subject.id)

    task_creator = TaskCreator(assignment, Repository[Task](Task, session))
    created_task = await task_creator.create(CreateTaskSchema(task_name=task_name,
                                                              points=points,
                                                              assignment_id=assignment.id))

    return created_task
