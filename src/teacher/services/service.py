from src.core.database.repo import Repository

from src.teacher.models import Teacher
from src.teacher.schemas import CreateTeacherSchema
from src.teacher.exceptions import TeacherNotFoundError


class TeacherService:
    def __init__(
            self,
            repo: Repository[Teacher],
    ):
        self.repo = repo

    async def delete(self, teacher_id: int) -> None:
        if await self.repo.get(id=teacher_id):
            return await self.repo.delete(teacher_id)
        raise TeacherNotFoundError()

    async def get_by_id(self, teacher_id: int) -> Teacher:
        teacher = await self.repo.get(id=teacher_id)
        if teacher:
            return teacher
        raise TeacherNotFoundError()

    async def update(self, teacher_id: int, new_data: CreateTeacherSchema) -> Teacher:
        teacher = await self.repo.get(id=teacher_id)
        if teacher:
            await self.repo.update(teacher_id, new_data.model_dump())
            return await self.repo.get(id=teacher_id)
        raise TeacherNotFoundError()
