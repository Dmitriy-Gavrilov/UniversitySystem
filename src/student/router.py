from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession

from .service import StudentService
from .schemas import CreateStudentSchema, StudentSchema
from src.core.database.dependencies import get_session


router = APIRouter(prefix="/students", tags=["Students"])


@router.get("/", summary="Получить всех студентов", response_model=list[StudentSchema])
async def get_all_students(session: AsyncSession = Depends(get_session)):
    service = StudentService(session)
    return await service.get_all_students()


@router.get("/{student_id}", summary="Получить данные конкретного студента", response_model=StudentSchema)
async def get_student_by_id(student_id: int, session: AsyncSession = Depends(get_session)):
    service = StudentService(session)
    return await service.get_student_by_id(student_id)


@router.post("/", summary="Создать студента", response_model=StudentSchema, status_code=status.HTTP_201_CREATED)
async def create_student(
        student_data: CreateStudentSchema,
        login: str,
        session: AsyncSession = Depends(get_session)
):
    service = StudentService(session)
    return await service.create_student(student_data)


@router.delete("/{student_id}", summary="Удалить студента", response_model=int)
async def delete_student(student_id: int, session: AsyncSession = Depends(get_session)):
    service = StudentService(session)
    await service.delete_student(student_id)
    return student_id


@router.put("/{student_id}", summary="Обновить данные студента", response_model=StudentSchema)
async def update_student(
        student_id: int,
        student_data: CreateStudentSchema,
        session: AsyncSession = Depends(get_session)
):
    service = StudentService(session)
    return await service.update_student(student_id, student_data)
