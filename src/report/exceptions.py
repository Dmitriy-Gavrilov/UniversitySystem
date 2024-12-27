from src.base.exceptions import BaseAppException


class ReportAlreadyExistsError(BaseAppException):
    def __init__(self):
        super().__init__(status_code=400, detail="Отчет уже существует")


class ReportNotFoundError(BaseAppException):
    def __init__(self):
        super().__init__(status_code=404, detail="Отчет не найден")
