from src.assignment.models import Assignment
from src.core.database.repo import Repository
from src.subject.models import Subject

from src.teacher.models import Teacher
from src.teacher.schemas import CreateTeacherSchema, ResponseTeacherSchema
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

    async def get_full_info(self, teacher_id: int, assignment_repo: Repository[Assignment],
                            subject_repo: Repository[Subject]) -> ResponseTeacherSchema:
        teacher = await self.repo.get(id=teacher_id)
        if not teacher:
            raise TeacherNotFoundError()

        assignments = await assignment_repo.get_all(filters=[Assignment.teacher_id == teacher_id])

        subjects = [(await subject_repo.get(id=a.subject_id)).subject_name for a in assignments]

        teacher_data = {key: getattr(teacher, key) for key in teacher.__mapper__.c.keys()}
        teacher_data["subjects"] = subjects

        return ResponseTeacherSchema(**teacher_data)

    async def update(self, teacher_id: int, new_data: CreateTeacherSchema) -> Teacher:
        teacher = await self.repo.get(id=teacher_id)
        if teacher:
            await self.repo.update(teacher_id, new_data.model_dump())
            return await self.repo.get(id=teacher_id)
        raise TeacherNotFoundError()
