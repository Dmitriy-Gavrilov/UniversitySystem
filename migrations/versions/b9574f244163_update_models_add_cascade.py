"""Update models: add cascade

Revision ID: b9574f244163
Revises: 94e1deff5bb1
Create Date: 2024-12-24 16:42:20.961498

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'b9574f244163'
down_revision: Union[str, None] = '94e1deff5bb1'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint('administrator_user_id_fkey', 'administrator', type_='foreignkey')
    op.create_foreign_key(None, 'administrator', 'user', ['user_id'], ['id'], ondelete='CASCADE')
    op.add_column('assignment', sa.Column('time', sa.DateTime(), nullable=False))
    op.drop_constraint('assignment_subject_id_fkey', 'assignment', type_='foreignkey')
    op.drop_constraint('assignment_group_id_fkey', 'assignment', type_='foreignkey')
    op.drop_constraint('assignment_teacher_id_fkey', 'assignment', type_='foreignkey')
    op.create_foreign_key(None, 'assignment', 'university_group', ['group_id'], ['id'], ondelete='CASCADE')
    op.create_foreign_key(None, 'assignment', 'teacher', ['teacher_id'], ['id'], ondelete='CASCADE')
    op.create_foreign_key(None, 'assignment', 'subject', ['subject_id'], ['id'], ondelete='CASCADE')
    op.drop_constraint('report_task_id_fkey', 'report', type_='foreignkey')
    op.drop_constraint('report_student_id_fkey', 'report', type_='foreignkey')
    op.create_foreign_key(None, 'report', 'task', ['task_id'], ['id'], ondelete='CASCADE')
    op.create_foreign_key(None, 'report', 'student', ['student_id'], ['id'], ondelete='CASCADE')
    op.drop_constraint('statistics_subject_id_fkey', 'statistics', type_='foreignkey')
    op.drop_constraint('statistics_teacher_id_fkey', 'statistics', type_='foreignkey')
    op.drop_constraint('statistics_student_id_fkey', 'statistics', type_='foreignkey')
    op.create_foreign_key(None, 'statistics', 'subject', ['subject_id'], ['id'], ondelete='CASCADE')
    op.create_foreign_key(None, 'statistics', 'student', ['student_id'], ['id'], ondelete='CASCADE')
    op.create_foreign_key(None, 'statistics', 'teacher', ['teacher_id'], ['id'], ondelete='SET NULL')
    op.drop_constraint('student_user_id_fkey', 'student', type_='foreignkey')
    op.drop_constraint('student_group_id_fkey', 'student', type_='foreignkey')
    op.create_foreign_key(None, 'student', 'user', ['user_id'], ['id'], ondelete='CASCADE')
    op.create_foreign_key(None, 'student', 'university_group', ['group_id'], ['id'], ondelete='CASCADE')
    op.drop_constraint('task_assignment_id_fkey', 'task', type_='foreignkey')
    op.create_foreign_key(None, 'task', 'assignment', ['assignment_id'], ['id'], ondelete='CASCADE')
    op.drop_constraint('teacher_user_id_fkey', 'teacher', type_='foreignkey')
    op.create_foreign_key(None, 'teacher', 'user', ['user_id'], ['id'], ondelete='CASCADE')
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'teacher', type_='foreignkey')
    op.create_foreign_key('teacher_user_id_fkey', 'teacher', 'user', ['user_id'], ['id'])
    op.drop_constraint(None, 'task', type_='foreignkey')
    op.create_foreign_key('task_assignment_id_fkey', 'task', 'assignment', ['assignment_id'], ['id'])
    op.drop_constraint(None, 'student', type_='foreignkey')
    op.drop_constraint(None, 'student', type_='foreignkey')
    op.create_foreign_key('student_group_id_fkey', 'student', 'university_group', ['group_id'], ['id'])
    op.create_foreign_key('student_user_id_fkey', 'student', 'user', ['user_id'], ['id'])
    op.drop_constraint(None, 'statistics', type_='foreignkey')
    op.drop_constraint(None, 'statistics', type_='foreignkey')
    op.drop_constraint(None, 'statistics', type_='foreignkey')
    op.create_foreign_key('statistics_student_id_fkey', 'statistics', 'student', ['student_id'], ['id'])
    op.create_foreign_key('statistics_teacher_id_fkey', 'statistics', 'teacher', ['teacher_id'], ['id'])
    op.create_foreign_key('statistics_subject_id_fkey', 'statistics', 'subject', ['subject_id'], ['id'])
    op.drop_constraint(None, 'report', type_='foreignkey')
    op.drop_constraint(None, 'report', type_='foreignkey')
    op.create_foreign_key('report_student_id_fkey', 'report', 'student', ['student_id'], ['id'])
    op.create_foreign_key('report_task_id_fkey', 'report', 'task', ['task_id'], ['id'])
    op.drop_constraint(None, 'assignment', type_='foreignkey')
    op.drop_constraint(None, 'assignment', type_='foreignkey')
    op.drop_constraint(None, 'assignment', type_='foreignkey')
    op.create_foreign_key('assignment_teacher_id_fkey', 'assignment', 'teacher', ['teacher_id'], ['id'])
    op.create_foreign_key('assignment_group_id_fkey', 'assignment', 'university_group', ['group_id'], ['id'])
    op.create_foreign_key('assignment_subject_id_fkey', 'assignment', 'subject', ['subject_id'], ['id'])
    op.drop_column('assignment', 'time')
    op.drop_constraint(None, 'administrator', type_='foreignkey')
    op.create_foreign_key('administrator_user_id_fkey', 'administrator', 'user', ['user_id'], ['id'])
    # ### end Alembic commands ###