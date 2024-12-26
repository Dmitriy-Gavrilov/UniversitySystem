from src.core.database.repo import Repository

from src.subject.models import Subject
from src.subject.schemas import CreateSubjectSchema
from src.subject.exceptions import SubjectNotFoundError, SubjectAlreadyExistsError


class SubjectService:
    def __init__(
            self,
            repo: Repository[Subject],
    ):
        self.repo = repo

    async def create(self, subject: CreateSubjectSchema) -> Subject:
        subject_model = Subject(
            subject_name=subject.subject_name
        )
        if await self.repo.get(**subject.model_dump()):
            raise SubjectAlreadyExistsError()
        await self.repo.create(subject_model)
        return await self.repo.get(**subject.model_dump())

    async def delete(self, subject_id: int) -> None:
        if await self.repo.get(id=subject_id):
            return await self.repo.delete(subject_id)
        raise SubjectNotFoundError()
