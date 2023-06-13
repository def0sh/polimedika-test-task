
from typing import List, Optional

from pydantic import BaseModel, Field


class InputCourse(BaseModel):
    course_name: str = Field(example="Алгебра")


class OutGrade(BaseModel):
    id: int
    student_id: int
    course_id: int
    grade: int

    class Config:
        orm_mode = True


class InputStudent(BaseModel):
    name: str = Field(example='Алексей')
    surname: str = Field(example='Тестов')

    class Config:
        orm_mode = True


class OutStudent(BaseModel):
    id: int
    name: str
    surname_name: str
    courses: Optional[List[str]]
    grade: Optional[List[str]]

    class Config:
        orm_mode = True


class OutStudPost(BaseModel):
    id: int
    name: str
    surname_name: str

    class Config:
        orm_mode = True


class OutStud(BaseModel):
    id: int
    name: str
    surname_name: str

    class Config:
        orm_mode = True


class Teacher(BaseModel):
    name: str
    surname: str


class OutTeacher(BaseModel):
    id: int
    name: str
    surname_name: str
    phone: str

    class Config:
        orm_mode = True


class InputGrade(BaseModel):
    id: int
    student_id: int = Field(example=1)
    course_id: int = Field(example=1)
    grade: int = Field(example=5)


class OutCourse(BaseModel):
    id: int
    course_name: str

    class Config:
        orm_mode = True

