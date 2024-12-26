from src.base.exceptions import BaseAppException


class TeacherAlreadyExistsError(BaseAppException):
    def __init__(self):
        super().__init__(status_code=400, detail="Преподаватель уже существует")


class TeacherNotFoundError(BaseAppException):
    def __init__(self):
        super().__init__(status_code=404, detail="Преподаватель не найден")
