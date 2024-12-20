from fastapi import APIRouter, Request
from fastapi import Depends
from starlette.templating import Jinja2Templates
from app.schemas.reservation_schema import ReservationSchema
from application.dto.reservation_dto import ReservationDto
from application.services.reservation_service import ReservationService
from app.schemas.schemas import ReservationBase
from infrastructure.providers.provider_module import get_reservation_service

router = APIRouter()
templates = Jinja2Templates(directory="app/templates")

@router.post("/reservations")
def create_reservation(request:Request, reservation_dto: ReservationDto, reservation_service: ReservationService = Depends(get_reservation_service)):
    reservation_dto.user_id = request.state.user["id"]
    return reservation_service.create(reservation_dto)
    

@router.get("/reservations")
def get_reservations(reservation_service: ReservationService = Depends(get_reservation_service)):
    return reservation_service.get_all()

@router.get("/reservations/{reservation_id}")
def get_reservation(reservation_id: int, reservation_service: ReservationService = Depends(get_reservation_service)):
    return reservation_service.get_one(reservation_id)

@router.put("/reservations")
def update_reservation(reservation: ReservationBase, reservation_service: ReservationService = Depends(get_reservation_service)):
    return reservation_service.update(reservation)

@router.get("/user/reservations")
def get_reservations_by_user(request: Request, reservation_service: ReservationService = Depends(get_reservation_service)):
    return reservation_service.get_by_user(request.state.user["id"])

@router.get("/confirmed/reservations/")
def get_confirmed_reservations_by_user(reservation_service: ReservationService = Depends(get_reservation_service)):
    return reservation_service.get_confirmed_reservations()

@router.post("/reservations/{reservation_id}/confirm")
def confirm_reservation(reservation_id: int, reservation_service: ReservationService = Depends(get_reservation_service)):
    return reservation_service.confirm_reservation(reservation_id)

@router.post("/reservations/{reservation_id}/cancel")
def cancel_reservation(reservation_id: int, reservation_service: ReservationService = Depends(get_reservation_service)):
    return reservation_service.cancel_reservation(reservation_id)

@router.post("/reservations/{reservation_id}/finalize")
def finalize_reservation(reservation_id: int, reservation_service: ReservationService = Depends(get_reservation_service)):
    return reservation_service.finalize_reservation(reservation_id)

@router.get("/reservations/orders/{reservation_id}")
def get_orders_by_reservation(reservation_id: int, reservation_service: ReservationService = Depends(get_reservation_service)):
    return reservation_service.get_orders_by_reservation(reservation_id)