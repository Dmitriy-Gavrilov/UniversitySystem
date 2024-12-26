from datetime import datetime

from src.assignment.models import Assignment
from src.core.database.repo import Repository
from src.group.models import UniversityGroup
from src.subject.models import Subject
from src.assignment.schemas import AssignmentCreateSchema, BaseAssignmentSchema
from src.assignment.exceptions import TimeConflictError
from src.teacher.models import Teacher


class AssignmentCreator:
    def __init__(
            self,
            subject: Subject,
            teacher: Teacher,
            group: UniversityGroup,
            repo: Repository[Assignment],
    ):
        self.repo = repo
        self.subject = subject
        self.teacher = teacher
        self.group = group

    async def create(self, assignment: AssignmentCreateSchema) -> Assignment:
        time = datetime.combine(assignment.date, assignment.time)
        assignment_dict = {
            "subject_id": self.subject.id,
            "work_type": assignment.work_type,
            "teacher_id": self.teacher.id,
            "group_id": self.group.id,
            "time": time
        }
        assignment_model = Assignment(**assignment_dict)
        await self._check_time(time)
        await self.repo.create(assignment_model)
        return await self.repo.get(**assignment_dict)

    async def _check_time(self, time: datetime) -> bool:
        all_assignments = await self.repo.get_all(filters=[Assignment.time == time])
        if all_assignments:
            for a in all_assignments:
                if a.teacher_id == self.teacher.id:
                    raise TimeConflictError("Преподаватель занят в это время")
                elif a.group_id == self.group.id:
                    raise TimeConflictError("Группа занята в это время")
        return True
