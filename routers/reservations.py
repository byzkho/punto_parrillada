from fastapi import APIRouter, Request
from fastapi import Depends
from sqlalchemy.orm import Session
from starlette.templating import Jinja2Templates

from app.config.database.database import get_db
from app.schemas.schemas import ReservationBase
from crud import reservations as crud

router = APIRouter()
templates = Jinja2Templates(directory="app/templates")

@router.post("/reservations")
def create_reservation(reservation: ReservationBase, db: Session = Depends(get_db)):
    return crud.create_reservation(db=db, reservation=reservation)

@router.get("/reservations/{reservation_id}")
def get_reservation(reservation_id: int, db: Session = Depends(get_db)):
    return crud.get_reservation(db=db, reservation_id=reservation_id)
