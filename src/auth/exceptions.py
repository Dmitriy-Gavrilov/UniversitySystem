from src.base.exceptions import BaseAppException


class OtherRoleRequired(BaseAppException):
    def __init__(self):
        super().__init__(status_code=401, detail="У пользователя другая роль")