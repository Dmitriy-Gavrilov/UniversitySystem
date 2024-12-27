from fastapi import APIRouter, Depends, status, Request
from sqlalchemy.ext.asyncio import AsyncSession

from src.auth.router import security
from src.core.database.repo import Repository
from src.core.database.dependencies import get_session
from src.settings import JWT_ACCESS_COOKIE_NAME

from src.subject.models import Subject
from src.subject.schemas import CreateSubjectSchema, SubjectSchema
from src.subject.services.service import SubjectService

router = APIRouter(prefix="/subjects", tags=["Subjects"])


@router.get(
    path="/",
    summary="Получить список всех предметов",
    response_model=list[SubjectSchema],
    dependencies=[Depends(security.access_token_required)],
)
async def get_all_subjects(request: Request, session: AsyncSession = Depends(get_session)):
    token = await security.get_access_token_from_request(request)
    security.verify_token(token, verify_csrf=False)

    repo = Repository[Subject](Subject, session)
    subjects = await repo.get_all()
    return [SubjectSchema.model_validate(subject) for subject in subjects]


@router.post(
    path="/",
    summary="Создать предмет",
    response_model=SubjectSchema,
    status_code=status.HTTP_201_CREATED,
    dependencies=[Depends(security.access_token_required)],
)
async def create_subject(
        subject_data: CreateSubjectSchema,
        request: Request,
        session: AsyncSession = Depends(get_session)
):
    token = await security.get_access_token_from_request(request)
    security.verify_token(token, verify_csrf=False)

    subject_service = SubjectService(Repository[Subject](Subject, session))
    created_subject = await subject_service.create(subject_data)

    return created_subject


@router.delete(
    path="/{subject_id}",
    summary="Удалить предмет",
    response_model=int,
    dependencies = [Depends(security.access_token_required)],
)
async def delete_subject(
        subject_id: int,
        request: Request,
        session: AsyncSession = Depends(get_session)
):
    token = await security.get_access_token_from_request(request)
    security.verify_token(token, verify_csrf=False)

    subject_service = SubjectService(Repository[Subject](Subject, session))
    await subject_service.delete(subject_id)
    return subject_id
