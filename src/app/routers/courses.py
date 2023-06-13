from typing import List

from fastapi import APIRouter, HTTPException, Depends
from pydantic import parse_obj_as
from sqlalchemy.orm import Session
from starlette import status

from src.app.crud.crud import get_course_by_name, get_students_course
from src.app.models import Course
from src.app.schemas import InputCourse, OutCourse, OutStud
from src.database import get_db

router = APIRouter(
    prefix="/courses",
    tags=["Courses"],
    responses={404: {"description": "Not found"}},
)


@router.post("/", status_code=status.HTTP_201_CREATED)
def create_course(course: InputCourse, db: Session = Depends(get_db)) -> OutCourse:
    """Создать новый курс"""

    crs = get_course_by_name(db, course.course_name)
    if crs is None:
        new_course = Course(course_name=course.course_name)
        db.add(new_course)
        db.commit()
    else:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Курс уже существует")
    return new_course


@router.get("/{course_id}", status_code=status.HTTP_200_OK)
def get_course(course_id: int, db: Session = Depends(get_db)) -> OutCourse:
    """Получить информацию о курсе по id"""

    course = db.query(Course).filter(Course.id == course_id).first()
    if course:
        return course
    else:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Курс не найден")


@router.get("/{course_id}/students", status_code=status.HTTP_200_OK)
def get_course_students(course_id: int, db: Session = Depends(get_db)) -> List[OutStud]:
    """Получить список всех студентов на курсе"""

    all_stud_course = get_students_course(db, course_id)
    if not all_stud_course:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Студента или курса не существует")
    all_stud = parse_obj_as(List[OutStud], all_stud_course)

    return all_stud