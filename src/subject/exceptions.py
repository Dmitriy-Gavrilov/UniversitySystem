from src.base.exceptions import BaseAppException


class SubjectAlreadyExistsError(BaseAppException):
    def __init__(self):
        super().__init__(status_code=400, detail="Предмет уже существует")


class SubjectNotFoundError(BaseAppException):
    def __init__(self):
        super().__init__(status_code=404, detail="Предмет не найден")
