from src.core.database.repo import Repository
from src.student.models import Student
from src.student.exceptions import StudentNotFoundError
from src.student.schemas import CreateStudentSchema


class StudentService:
    def __init__(
            self,
            repo: Repository[Student],
    ):
        self.repo = repo

    async def delete(self, student_id: int) -> None:
        if await self.repo.get(id=student_id):
            return await self.repo.delete(student_id)
        raise StudentNotFoundError

    async def get_by_id(self, student_id: int) -> Student:
        student = await self.repo.get(id=student_id)
        if student:
            return student
        raise StudentNotFoundError

    async def update(self, student_id: int, new_data: CreateStudentSchema) -> Student:
        student = await self.repo.get(id=student_id)
        if student:
            await self.repo.update(student_id, new_data.model_dump())
            return await self.repo.get(id=student_id)
        raise StudentNotFoundError
