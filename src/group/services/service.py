from src.core.database.repo import Repository
from src.group.models import UniversityGroup
from src.group.schemas import GroupCreateSchema
from src.group.exceptions import GroupAlreadyExistsError, GroupNotFoundError


class GroupService:
    def __init__(
            self,
            repo: Repository[UniversityGroup],
    ):
        self.repo = repo

    async def create(self, group: GroupCreateSchema) -> UniversityGroup:
        group_model = UniversityGroup(group_name=group.group_name)

        if await self.repo.get(group_name=group.group_name):
            raise GroupAlreadyExistsError()

        await self.repo.create(group_model)
        created_group = await self.repo.get(group_name=group.group_name)
        return created_group

    async def delete(self, group_id: int) -> None:
        group = await self.repo.get(id=group_id)
        if group:
            return await self.repo.delete(group_id)
        raise GroupNotFoundError()

    async def get_by_id(self, group_id: int) -> UniversityGroup:
        group = await self.repo.get(id=group_id)
        if group:
            return group
        raise GroupNotFoundError()
