from fastapi import APIRouter, Request
from fastapi import Depends
from sqlalchemy.orm import Session
from starlette.templating import Jinja2Templates

from application.dto.reservation_dto import ReservationDto
from application.services.reservation_service import ReservationService
from infrastructure.database.database import get_db
from app.schemas.schemas import ReservationBase
from crud import reservations as crud
from infrastructure.database.models import TableStatus
from infrastructure.providers.provider_module import get_reservation_service

router = APIRouter()
templates = Jinja2Templates(directory="app/templates")

@router.post("/reservations")
def create_reservation(request:Request, reservation_dto: ReservationDto, reservation_service: ReservationService = Depends(get_reservation_service)):
    # return crud.create_reservation(db=db, reservation=reservation_data)
    reservation_dto.user_id = request.state.user["id"]
    return reservation_service.create(reservation_dto)

@router.get("/reservations/{reservation_id}")
def get_reservation(reservation_id: int, db: Session = Depends(get_db)):
    return crud.get_reservation(db=db, reservation_id=reservation_id)