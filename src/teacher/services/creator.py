from src.core.database.repo import Repository
from src.teacher.models import Teacher
from src.teacher.schemas import CreateTeacherSchema
from src.teacher.exceptions import TeacherAlreadyExistsError
from src.user.models import User


class TeacherCreator:
    def __init__(
            self,
            user: User,
            repo: Repository[Teacher],
    ):
        self.repo = repo
        self.user = user

    async def create(self, teacher: CreateTeacherSchema) -> Teacher:
        teacher_model = Teacher(
            user_id=self.user.id,
            surname=teacher.surname,
            name=teacher.name,
            patronym=teacher.patronym,
        )
        if await self.repo.get(**teacher.model_dump()):
            raise TeacherAlreadyExistsError()
        await self.repo.create(teacher_model)
        return await self.repo.get(**teacher.model_dump())
