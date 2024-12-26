from src.core.database.repo import Repository
from src.teacher.exceptions import TeacherNotFoundError
from src.teacher.models import Teacher


class TeacherGetter:
    def __init__(self, repo: Repository[Teacher]):
        self.repo = repo

    async def get_by_full_name(self, surname: str, name: str, patronym: str) -> Teacher:
        existing_teacher = await self.repo.get(surname=surname,
                                               name=name,
                                               patronym=patronym)
        if existing_teacher:
            return existing_teacher
        raise TeacherNotFoundError()
