from src.base.exceptions import BaseAppException


class AssignmentAlreadyExistsError(BaseAppException):
    def __init__(self):
        super().__init__(status_code=400, detail="Занятие уже существует")


class AssignmentNotFoundError(BaseAppException):
    def __init__(self):
        super().__init__(status_code=404, detail="Занятие не найдено")


class TimeConflictError(BaseAppException):
    def __init__(self, detail: str):
        super().__init__(status_code=400, detail=detail)