from src.core.database.repo import Repository
from src.core.password_hasher import Hasher
from src.user.models import User
from src.user.exceptions import UserNotFoundError, WrongUserPassword


class UserGetter:
    def __init__(self, repo: Repository[User]):
        self.repo = repo

    async def get_for_login(self, login: str, password: str) -> User:
        if existing_user := await self.repo.get(login=login):
            if Hasher().verify_password(password, existing_user.password):
                return existing_user
            raise WrongUserPassword()
        raise UserNotFoundError()
