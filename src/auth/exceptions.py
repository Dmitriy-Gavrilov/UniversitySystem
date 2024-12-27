from src.base.exceptions import BaseAppException


class OtherRoleRequired(BaseAppException):
    def __init__(self):
        super().__init__(status_code=403, detail="У пользователя другая роль")


class AdminRoleRequired(BaseAppException):
    def __init__(self):
        super().__init__(status_code=403, detail="У пользователя другая роль")


class TeacherRoleRequired(BaseAppException):
    def __init__(self):
        super().__init__(status_code=403, detail="У пользователя другая роль")
