from typing import List

from fastapi import APIRouter, Depends
from pydantic import parse_obj_as
from sqlalchemy.orm import Session
from starlette import status

from src.app.crud.crud import get_all_teachers
from src.app.schemas import OutTeacher
from src.database import get_db

router = APIRouter(
    prefix="/teachers",
    tags=["Teacher"],
    responses={404: {"description": "Not found"}},

)


@router.get("/", status_code=status.HTTP_200_OK)
def get_teachers(db: Session = Depends(get_db)) -> List[OutTeacher]:
    """Получить список всех преподавателей"""

    teachers = get_all_teachers(db)

    res = parse_obj_as(List[OutTeacher], teachers)
    return res
