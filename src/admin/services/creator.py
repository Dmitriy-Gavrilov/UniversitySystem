from src.core.database.repo import Repository
from src.admin.models import Administrator
from src.admin.schemas import AdminCreateSchema
from src.admin.exceptions import AdminAlreadyExistsError
from src.user.models import User


class AdminCreator:
    def __init__(
            self,
            user: User,
            repo: Repository[Administrator],
    ):
        self.repo = repo
        self.user = user

    async def create(self, admin: AdminCreateSchema) -> Administrator:
        admin_model = Administrator(
            user_id=self.user.id,
            surname=admin.surname,
            name=admin.name,
            patronym=admin.patronym,
        )
        if await self.repo.get(**admin.model_dump()):
            raise AdminAlreadyExistsError()
        await self.repo.create(admin_model)
        return await self.repo.get(**admin.model_dump())