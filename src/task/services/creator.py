from src.assignment.models import Assignment
from src.core.database.repo import Repository
from src.task.models import Task
from src.task.schemas import CreateTaskSchema
from src.task.exceptions import TaskAlreadyExistsError


class TaskCreator:
    def __init__(
            self,
            assignment: Assignment,
            repo: Repository[Task],
    ):
        self.repo = repo
        self.assignment = assignment

    async def create(self, task: CreateTaskSchema) -> Task:
        task_model = Task(task_name=task.task_name,
                          points=task.points,
                          assignment_id=task.assignment_id)
        if await self.repo.get(**task.model_dump()):
            raise TaskAlreadyExistsError
        await self.repo.create(task_model)
        return await self.repo.get(**task.model_dump())
