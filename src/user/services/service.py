from src.core.database.repo import Repository
from src.user.models import User
from src.user.schemas import CreateUserSchema
from src.core.password_hasher import Hasher
from src.user.exceptions import UserAlreadyExistsError, UserNotFoundError


class UserService:
    def __init__(
            self,
            repo: Repository[User],
    ):
        self.repo = repo

    async def create(self, user: CreateUserSchema) -> User:
        user_model = User(
            login=user.login,
            password=Hasher.get_password_hash(user.password),
            role=user.role
        )
        if await self.repo.get(login=user.login):
            raise UserAlreadyExistsError
        await self.repo.create(user_model)
        created_user = await self.repo.get(login=user.login)
        return created_user

    async def delete(self, user_id: int) -> None:
        if await self.repo.get(id=user_id):
            return await self.repo.delete(user_id)
        raise UserNotFoundError

    async def get_by_id(self, user_id: int) -> User:
        user = await self.repo.get(id=user_id)
        if user:
            return user
        raise UserNotFoundError
