from sqlalchemy import Column, Integer, String, Table, ForeignKey
from sqlalchemy.orm import relationship

from src.database import Base


student_course = Table(
    'student_course',
    Base.metadata,
    Column('student_id', ForeignKey('student.id')),
    Column('course_id', ForeignKey('course.id')),

)


class Student(Base):
    __tablename__ = "student"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    surname_name = Column(String, nullable=False)
    courses = relationship('Course', secondary=student_course)
    grade = relationship("Grade", back_populates="student")

    def __repr__(self):
        return f'Student {self.name} {self.surname_name}'


class Course(Base):
    __tablename__ = "course"

    id = Column(Integer, primary_key=True, index=True)
    course_name = Column(String(100), nullable=False)
    student = relationship('Student', secondary=student_course)
    grade = relationship("Grade", back_populates="course")

    def __repr__(self):
        return f'Course {self.course_name}'


class Grade(Base):
    __tablename__ = "grade"

    id = Column(Integer, primary_key=True)
    student_id = Column(Integer, ForeignKey("student.id"), nullable=False)
    course_id = Column(Integer, ForeignKey("course.id"), nullable=False)
    grade = Column(Integer, nullable=False)
    student = relationship("Student", back_populates="grade")
    course = relationship("Course", back_populates="grade")

    def __repr__(self):
        return f'Grade {self.grade}'


class Teacher(Base):
    __tablename__ = "teacher"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(20), nullable=False)
    surname_name = Column(String(20), nullable=False)
    phone = Column(String(15), nullable=False)

    def __repr__(self):
        return f'Teacher {self.name} {self.surname_name}'





