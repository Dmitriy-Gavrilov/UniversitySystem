from fastapi import APIRouter, Depends, status, Query
from sqlalchemy.ext.asyncio import AsyncSession

from src.core.database.dependencies import get_session
from src.core.database.repo import Repository
from src.report.models import Report

from src.report.schemas import ReportSchema, CreateReportSchema, UpdateReportSchema
from src.report.services.creator import ReportCreator
from src.report.services.service import ReportService
from src.task.services.service import TaskService
from src.task.models import Task

router = APIRouter(prefix="/reports", tags=["Reports"])


# @router.get("/", summary="Получить все отчеты", response_model=list[ReportSchema])
# async def get_all_reports(
#         session: AsyncSession = Depends(get_session)):
#     pass


@router.get("/", summary="Получить все отчеты", response_model=list[ReportSchema])
async def get_all_reports(
        student_id: int | None = Query(None, description="ID студента для фильтрации"),
        task_id: int | None = Query(None, description="ID задания для фильтрации"),
        session: AsyncSession = Depends(get_session)):
    repo = Repository[Report](Report, session)

    filters = []
    if student_id:
        filters.append(Report.student_id == student_id)
    if task_id:
        filters.append(Report.task_id == task_id)

    reports = await repo.get_all(filters=filters)
    return reports


@router.post("/", summary="Добавить отчет", response_model=ReportSchema, status_code=status.HTTP_201_CREATED)
async def create_report(
        report_data: CreateReportSchema,
        session: AsyncSession = Depends(get_session)
):
    report_creator = ReportCreator(Repository[Report](Report, session))
    created_report = await report_creator.create(report_data)

    return created_report


@router.delete("/{report_id}", summary="Удалить отчет", response_model=int)
async def delete_report(
        report_id: int,
        session: AsyncSession = Depends(get_session)):
    report_servie = ReportService(Repository[Report](Report, session))
    await report_servie.delete(report_id)
    return report_id


@router.patch("/{report_id}", summary="Обновить данные отчета", response_model=ReportSchema)
async def update_report(
        report_id: int,
        report_data: UpdateReportSchema,
        session: AsyncSession = Depends(get_session)
):
    report_service = ReportService(Repository[Report](Report, session))
    updated_report = await report_service.update(report_id, report_data)
    return updated_report
