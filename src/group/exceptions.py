from src.base.exceptions import BaseAppException


class GroupAlreadyExistsError(BaseAppException):
    def __init__(self):
        super().__init__(status_code=400, detail="Группа уже существует")


class GroupNotFoundError(BaseAppException):
    def __init__(self):
        super().__init__(status_code=404, detail="Группа не найдена")
