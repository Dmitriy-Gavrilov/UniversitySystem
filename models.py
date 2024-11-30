from sqlalchemy.orm import DeclarativeBase, relationship
from sqlalchemy import Column, Integer, String, ForeignKey, DateTime, func


class Base(DeclarativeBase):
    __abstract__ = True


class User(Base):
    __tablename__ = "user"

    user_id = Column(Integer, primary_key=True, autoincrement=True)
    login = Column(String(50), nullable=False, unique=True)
    password_hash = Column(String(128), nullable=False)
    role = Column(String(25), nullable=False)


class Student(Base):
    __tablename__ = "student"

    student_id = Column(Integer, primary_key=True, autoincrement=True)
    user_id = Column(Integer, ForeignKey('user.user_id'), nullable=False)
    surname = Column(String(50), nullable=False)
    name = Column(String(50), nullable=False)
    patronym = Column(String(50), nullable=False)
    group_id = Column(Integer, ForeignKey('university_group.group_id'))

    group = relationship("UniversityGroup", back_populates="students")


class UniversityGroup(Base):
    __tablename__ = "university_group"

    group_id = Column(Integer, primary_key=True, autoincrement=True)
    group_name = Column(String(25), nullable=False, unique=True)

    students = relationship("Student", back_populates="group")


class Teacher(Base):
    __tablename__ = "teacher"

    teacher_id = Column(Integer, primary_key=True, autoincrement=True)
    user_id = Column(Integer, ForeignKey('user.user_id'), nullable=False)
    surname = Column(String(50), nullable=False)
    name = Column(String(50), nullable=False)
    patronym = Column(String(50), nullable=False)


class Administrator(Base):
    __tablename__ = "administrator"

    admin_id = Column(Integer, primary_key=True, autoincrement=True)
    user_id = Column(Integer, ForeignKey('user.user_id'), nullable=False)
    surname = Column(String(50), nullable=False)
    name = Column(String(50), nullable=False)
    patronym = Column(String(50), nullable=False)


class Subject(Base):
    __tablename__ = "subject"

    subject_id = Column(Integer, primary_key=True, autoincrement=True)
    subject_name = Column(String(100), nullable=False, unique=True)


class WorkType(Base):
    __tablename__ = "worktype"

    work_type_id = Column(Integer, primary_key=True, autoincrement=True)
    work_type_name = Column(String(25), nullable=False, unique=True)


class Assignment(Base):
    __tablename__ = "assignment"

    assignment_id = Column(Integer, primary_key=True, autoincrement=True)
    subject_id = Column(Integer, ForeignKey('subject.subject_id'), nullable=False)
    work_type_id = Column(Integer, ForeignKey('worktype.work_type_id'), nullable=False)
    teacher_id = Column(Integer, ForeignKey('teacher.teacher_id'), nullable=False)
    group_id = Column(Integer, ForeignKey('university_group.group_id'), nullable=False)

    subject = relationship("Subject")
    work_type = relationship("WorkType")
    teacher = relationship("Teacher")
    group = relationship("UniversityGroup")


class Task(Base):
    __tablename__ = "task"

    task_id = Column(Integer, primary_key=True, autoincrement=True)
    task_name = Column(String(100), nullable=False)
    points = Column(Integer, nullable=False)
    assignment_id = Column(Integer, ForeignKey('assignment.assignment_id'))

    reports = relationship("Report", back_populates="task")


class Report(Base):
    __tablename__ = "report"

    report_id = Column(Integer, primary_key=True, autoincrement=True)
    report_name = Column(String(100), nullable=False)
    load_date = Column(DateTime, default=func.now(), nullable=False)
    accept_date = Column(DateTime, nullable=True)
    grade = Column(Integer, nullable=True)
    task_id = Column(Integer, ForeignKey('task.task_id'))
    student_id = Column(Integer, ForeignKey('student.student_id'))

    task = relationship("Task", back_populates="reports")
