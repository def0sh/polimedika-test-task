from sqlalchemy.orm import Session

from src.app import models
from src.app.models import Student, Course


# crud operations with students and teachers


def get_student(db: Session, surname: str):
    # return db.query(models.Stud).filter(models.Stud.id == user_id).first()
    return db.query(models.Student).filter(models.Student.surname_name == surname).first()


def get_student_id(db: Session, stud_id: int):
    # return db.query(models.Stud).filter(models.Stud.id == user_id).first()
    return db.query(models.Student).filter(models.Student.id == stud_id).first()


def get_all_teachers(db: Session):
    # return db.query(models.Teacher).offset(skip).limit(limit).all()
    return db.query(models.Teacher).all()


def get_students_course(db: Session, course_id):
    return db.query(Student).join(Student.courses).filter(Course.id == course_id).all()


def get_course_by_name(db: Session, course_name):
    return db.query(models.Course).filter(models.Course.course_name == course_name).first()



