from src.auth.exceptions import AdminRoleRequired, TeacherRoleRequired
from src.user.models import User, UserRole


class AuthRoleVerifier:
    def __init__(self, user: User):
        self.user = user

    def verify(self, required_role: UserRole) -> None:
        if required_role == UserRole.ADMIN and self.user.role != UserRole.ADMIN:
            raise AdminRoleRequired()
        elif required_role == UserRole.TEACHER and self.user.role == UserRole.STUDENT:
            raise TeacherRoleRequired()
        return
