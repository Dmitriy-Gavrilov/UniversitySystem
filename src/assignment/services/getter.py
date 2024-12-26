from typing import List

from src.core.database.repo import Repository
from src.assignment.exceptions import AssignmentNotFoundError
from src.assignment.models import Assignment


class AssignmentGetter:
    def __init__(self, repo: Repository[Assignment]):
        self.repo = repo

    async def get_by_parameters(self, filters: list) -> list[Assignment]:
        ass = await self.repo.get_all(filters=filters)
        if ass:
            return ass
        raise AssignmentNotFoundError()
