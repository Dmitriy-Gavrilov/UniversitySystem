from src.base.exceptions import BaseAppException


class TaskAlreadyExistsError(BaseAppException):
    def __init__(self):
        super().__init__(status_code=400, detail="Задание уже существует")


class TaskNotFoundError(BaseAppException):
    def __init__(self):
        super().__init__(status_code=404, detail="Задание не найдено")