from src.assignment.models import Assignment
from src.core.database.repo import Repository
from src.subject.models import Subject

from src.report.models import Report
from src.report.schemas import CreateReportSchema, UpdateReportSchema
from src.report.exceptions import ReportNotFoundError


class ReportService:
    def __init__(
            self,
            repo: Repository[Report],
    ):
        self.repo = repo

    async def delete(self, report_id: int) -> None:
        if await self.repo.get(id=report_id):
            return await self.repo.delete(report_id)
        raise ReportNotFoundError()

    async def get_by_id(self, report_id: int) -> Report:
        report = await self.repo.get(id=report_id)
        if report:
            return report
        raise ReportNotFoundError()

    async def update(self, report_id: int, new_data: UpdateReportSchema) -> Report:
        report = await self.repo.get(id=report_id)
        if not report:
            raise ReportNotFoundError()

        update_data = new_data.model_dump(exclude_unset=True)
        # update_data['check_date'] = datetime.now()  # Устанавливаем текущую дату проверки

        await self.repo.update(report_id, update_data)
        return await self.repo.get(id=report_id)
