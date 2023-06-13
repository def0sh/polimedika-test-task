
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from starlette import status

from src.app.crud.crud import get_student, get_student_id
from src.app.models import Student
from src.app.schemas import InputStudent, OutStudent, OutStud
from src.database import get_db

router = APIRouter(
    prefix="/students",
    tags=["Students"],
    responses={404: {"description": "Not found"}},

)


@router.post("/", status_code=status.HTTP_201_CREATED)
def create_student(student: InputStudent, db: Session = Depends(get_db)) -> OutStudent:
    """Создать нового студента"""

    stud = db.query(Student).filter(Student.name == student.name).first()
    if stud is None:
        new_student = Student(name=student.name, surname_name=student.surname)
        db.add(new_student)
        db.commit()
        created_student = get_student(db, surname=student.surname)

        return created_student
    else:
        raise HTTPException(status_code=400, detail="Студент уже существует")


@router.get("/{student_id}", status_code=status.HTTP_200_OK)
def read_student(student_id: int, db: Session = Depends(get_db)) -> OutStud:
    """Получить информацию о студенте по id"""

    user = get_student_id(db, stud_id=student_id)
    if user:
        return user
    else:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Студент не найден")


@router.put("/{student_id}", status_code=status.HTTP_201_CREATED)
def update_student(student_id: int, student: InputStudent, db: Session = Depends(get_db)) -> OutStud:
    """Обновить информацию о студенте по id"""

    stud = get_student_id(db, stud_id=student_id)
    if stud:
        stud.name = student.name
        stud.surname_name = student.surname
        db.add(stud)
        db.commit()

        res = get_student_id(db, stud_id=student_id)
        return res

    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Студент не найден")


@router.delete("/{student_id}", status_code=status.HTTP_200_OK)
def delete_student(student_id: int, db: Session = Depends(get_db)):
    """Удалить студента по id"""

    stud = get_student_id(db, stud_id=student_id)
    if stud:
        db.delete(stud)
        db.commit()
        return {'detail': 'Студент успешно удален'}
    else:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Студент не найден")