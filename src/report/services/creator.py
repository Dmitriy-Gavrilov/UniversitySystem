from src.assignment.models import Assignment
from src.core.database.repo import Repository
from src.report.models import Report
from src.report.schemas import CreateReportSchema
from src.task.models import Task
from src.task.schemas import CreateTaskSchema
from src.task.exceptions import TaskAlreadyExistsError


class ReportCreator:
    def __init__(
            self,
            repo: Repository[Report],
    ):
        self.repo = repo

    async def create(self, report: CreateReportSchema) -> Report:
        report_model = Report(report_name=report.report_name,
                              task_id=report.task_id,
                              student_id=report.student_id)
        existing_report = await self.repo.get(**report.model_dump())
        if existing_report and not existing_report.is_accepted:
            raise TaskAlreadyExistsError
        await self.repo.create(report_model)
        return await self.repo.get(**report.model_dump())
