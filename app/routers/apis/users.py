from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from sqlalchemy.sql import crud

from application.services.user_service import UserService
from infrastructure.database.database import get_db
from infrastructure.providers.provider_module import get_user_service

router = APIRouter()

@router.get("/users/")
def get_users(user_service: UserService = Depends(get_user_service)):
    return user_service.get_users()

@router.get("/users/{user_id}")
def get_user(user_id: int, db: Session = Depends(get_db)):
    return crud.get_user(db=db, user_id=user_id)
