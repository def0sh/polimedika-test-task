from fastapi import FastAPI, APIRouter
from starlette import status

from src.app.routers import courses, grades, teachers, students
from src.config import get_settings
from src.database import engine, Base


search_router = APIRouter(prefix='', tags=['University management system'])


def start_application():
    app = FastAPI(title=get_settings().APP_TITLE)
    app.include_router(search_router)
    return app


Base.metadata.create_all(bind=engine)

app = start_application()

app.include_router(courses.router)
app.include_router(grades.router)
app.include_router(teachers.router)
app.include_router(students.router)


@app.get("/", status_code=status.HTTP_200_OK)
def root() -> dict:
    return {"message": "Polimedika task", "docs": "/docs"}
