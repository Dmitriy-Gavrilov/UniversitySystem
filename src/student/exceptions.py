from src.base.exceptions import BaseAppException


class StudentAlreadyExistsError(BaseAppException):
    def __init__(self):
        super().__init__(status_code=400, detail="Студент уже существует")


class StudentNotFoundError(BaseAppException):
    def __init__(self):
        super().__init__(status_code=404, detail="Студент не найден")
