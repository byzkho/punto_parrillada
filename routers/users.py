from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from sqlalchemy.sql import crud

from app.database import get_db
from app.schemas import UserBase

router = APIRouter()

@router.post("/users/")
def create_user(user: UserBase, db: Session = Depends(get_db)):
    return crud.create_user(db=db, user=user)

@router.get("/users/{user_id}")
def get_user(user_id: int, db: Session = Depends(get_db)):
    return crud.get_user(db=db, user_id=user_id)
