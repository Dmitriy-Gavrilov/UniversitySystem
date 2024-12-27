from src.base.exceptions import BaseAppException


class UserAlreadyExistsError(BaseAppException):
    def __init__(self):
        super().__init__(status_code=400, detail="Пользователь уже существует")


class UserNotFoundError(BaseAppException):
    def __init__(self):
        super().__init__(status_code=404, detail="Пользователь не найден")


class WrongUserPassword(BaseAppException):
    def __init__(self):
        super().__init__(status_code=401, detail="Неверный пароль")
