from fastapi import Depends, APIRouter, HTTPException
from sqlalchemy.orm import Session
from starlette import status

from src.app.models import Grade
from src.app.schemas import InputGrade, OutGrade
from src.database import get_db

router = APIRouter(
    prefix="/grades",
    tags=["Grades"],
    responses={404: {"description": "Not found"}},
)


@router.post("/", status_code=status.HTTP_201_CREATED)
def create_grade(gr: InputGrade, db: Session = Depends(get_db)) -> OutGrade:
    """Создать новую оценку для студента по курсу"""

    grade_id = db.query(Grade).get(gr.id)
    if grade_id is not None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Оценка с таким id уже существует")
    grade = Grade(id=gr.id, grade=gr.grade, student_id=gr.student_id, course_id=gr.course_id)
    db.add(grade)
    db.commit()

    return grade


@router.put("/{grade_id}", status_code=status.HTTP_200_OK)
def update_grade(grade_id: int, gr: InputGrade, db: Session = Depends(get_db)) -> OutGrade:
    """Обновить оценку студента по курсу"""

    new_grade = db.query(Grade).filter_by(id=grade_id).first()
    if new_grade:
        new_grade.grade = gr.grade
        new_grade.student_id = gr.student_id
        new_grade.course_id = gr.course_id

        db.add(new_grade)
        db.commit()

        return new_grade
    else:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Неверные данные")