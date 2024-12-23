from src.core.database.repo import Repository
from src.group.models import UniversityGroup
from src.student.models import Student
from src.student.schemas import CreateStudentSchema
from src.student.exceptions import StudentAlreadyExistsError
from src.user.models import User


class StudentCreator:
    def __init__(
            self,
            user: User,
            group: UniversityGroup,
            repo: Repository[Student],
    ):
        self.repo = repo
        self.group = group
        self.user = user

    async def create(self, student: CreateStudentSchema) -> Student:
        student_model = Student(
            user_id=self.user.id,
            surname=student.surname,
            name=student.name,
            patronym=student.patronym,
            group=self.group,
        )
        if await self.repo.get(**student.model_dump()):
            raise StudentAlreadyExistsError
        await self.repo.create(student_model)
        return await self.repo.get(**student.model_dump())
