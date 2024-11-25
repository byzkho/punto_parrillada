from sqlalchemy.orm import Session
from infrastructure.database.models import Reservation
from app.schemas.schemas import ReservationBase

def create_reservation(db: Session, reservation: ReservationBase):
    db_reservation = Reservation(**reservation)
    db.add(db_reservation)
    db.commit()
    db.refresh(db_reservation)
    return db_reservation

def get_reservation(db: Session, reservation_id: int):
    return db.query(Reservation).filter(Reservation.id == reservation_id).first()
