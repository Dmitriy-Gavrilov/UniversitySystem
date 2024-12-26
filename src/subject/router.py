from fastapi import APIRouter, Depends, status
from sqlalchemy.ext.asyncio import AsyncSession

from src.core.database.repo import Repository
from src.core.database.dependencies import get_session

from src.subject.models import Subject
from src.subject.schemas import CreateSubjectSchema, SubjectSchema
from src.subject.services.service import SubjectService

router = APIRouter(prefix="/subjects", tags=["Subjects"])


@router.get("/", summary="Получить список всех предметов", response_model=list[SubjectSchema])
async def get_all_subjects(session: AsyncSession = Depends(get_session)):
    repo = Repository[Subject](Subject, session)
    subjects = await repo.get_all()
    return [SubjectSchema.model_validate(subject) for subject in subjects]


@router.post("/", summary="Создать предмет", response_model=SubjectSchema, status_code=status.HTTP_201_CREATED)
async def create_subject(
        subject_data: CreateSubjectSchema,
        session: AsyncSession = Depends(get_session)
):
    subject_service = SubjectService(Repository[Subject](Subject, session))
    created_subject = await subject_service.create(subject_data)

    return created_subject


@router.delete("/{subject_id}", summary="Удалить предмет", response_model=int)
async def delete_subject(
        subject_id: int,
        session: AsyncSession = Depends(get_session)):
    subject_service = SubjectService(Repository[Subject](Subject, session))
    await subject_service.delete(subject_id)
    return subject_id
