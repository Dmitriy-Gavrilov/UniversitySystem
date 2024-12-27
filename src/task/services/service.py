from src.core.database.repo import Repository

from src.task.models import Task
from src.task.exceptions import TaskNotFoundError


class TaskService:
    def __init__(
            self,
            repo: Repository[Task],
    ):
        self.repo = repo

    async def delete(self, task_id: int) -> None:
        if await self.repo.get(id=task_id):
            return await self.repo.delete(task_id)
        raise TaskNotFoundError()

    async def get_by_id(self, task_id: int) -> Task:
        task = await self.repo.get(id=task_id)
        if task:
            return task
        raise TaskNotFoundError()


