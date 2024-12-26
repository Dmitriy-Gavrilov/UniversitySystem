from src.base.exceptions import BaseAppException


class AdminAlreadyExistsError(BaseAppException):
    def __init__(self):
        super().__init__(status_code=400, detail="Администратор уже существует")


class AdminNotFoundError(BaseAppException):
    def __init__(self):
        super().__init__(status_code=404, detail="Администратор не найден")