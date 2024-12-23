from src.core.database.repo import Repository
from src.core.password_hasher import Hasher
from src.group.models import UniversityGroup


class GroupGetter:
    def __init__(self, repo: Repository[UniversityGroup]):
        self.repo = repo

    async def get_by_id(self, group_id: int) -> UniversityGroup:
        existing_group = await self.repo.get(id=group_id)
        if existing_group:
            return existing_group
        raise ValueError(f"Group with id {group_id} not found")