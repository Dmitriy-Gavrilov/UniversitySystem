from src.core.database.repo import Repository
from src.subject.exceptions import SubjectNotFoundError
from src.subject.models import Subject


class SubjectGetter:
    def __init__(self, repo: Repository[Subject]):
        self.repo = repo

    async def get_by_name(self, subject_name: str) -> Subject:
        existing_subject = await self.repo.get(subject_name=subject_name)
        if existing_subject:
            return existing_subject
        raise SubjectNotFoundError()
