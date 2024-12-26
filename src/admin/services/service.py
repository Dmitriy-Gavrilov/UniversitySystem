from src.core.database.repo import Repository

from src.admin.models import Administrator
from src.admin.schemas import AdminCreateSchema
from src.admin.exceptions import AdminNotFoundError


class AdminService:
    def __init__(
            self,
            repo: Repository[Administrator],
    ):
        self.repo = repo

    async def delete(self, admin_id: int) -> None:
        if await self.repo.get(id=admin_id):
            return await self.repo.delete(admin_id)
        raise AdminNotFoundError()

    async def get_by_id(self, admin_id: int) -> Administrator:
        admin = await self.repo.get(id=admin_id)
        if admin:
            return admin
        raise AdminNotFoundError()

    async def update(self, admin_id: int, new_data: AdminCreateSchema) -> Administrator:
        admin = await self.repo.get(id=admin_id)
        if admin:
            await self.repo.update(admin_id, new_data.model_dump())
            return await self.repo.get(id=admin_id)
        raise AdminNotFoundError()