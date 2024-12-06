from typing import List
from domain.repositories.reservation_repository import ReservationRepository
from infrastructure.database.models import Reservation, UserReservation
from sqlalchemy.orm import joinedload, Session


class ReservationRepositoryImpl(ReservationRepository):
    def __init__(self, session: Session):
        self.session = session

    def create(self, reservation: Reservation):
        entity = Reservation(**reservation)
        self.session.add(entity)
        self.session.commit()
        return reservation

    def get_one(self, reservation_id: int) -> Reservation:
        return self.session.query(Reservation).filter_by(id=reservation_id).options(
            joinedload(Reservation.table),
            joinedload(Reservation.user),
            joinedload(Reservation.orders)  # Cargar las órdenes asociadas
        ).first()

    def get_all(self) -> List[Reservation]:
        return self.session.query(Reservation).all()

    def update(self, reservation: Reservation):
        self.session.commit()

    def delete(self, reservation: Reservation):
        self.session.delete(reservation)
        self.session.commit()
        
    def get_by_user(self, user_id: int) -> List[Reservation]:
        return self.session.query(Reservation).filter_by(user_id=user_id).options(
            joinedload(Reservation.table),
            joinedload(Reservation.user),
            joinedload(Reservation.orders)  # Cargar las órdenes asociadas
        ).all()
    
    def create_user_table(self, table_id: int, user_id: int, reservated_at: str):
        user_table = UserReservation(user_id=user_id, table_id=table_id, reservated_at=reservated_at)
        self.session.add(user_table)
        self.session.commit()
        return user_table
    
    def get_confirmed_reservations_by_user(self, user_id: int) -> List:
        return self.session.query(Reservation).filter(Reservation.user_id == user_id).filter(Reservation.status == 'CONFIRMADA').first()
    
    def update_status_reservation(self, reservation_id: int, status: str):
        print(status)
        reservation = self.session.query(Reservation).filter(Reservation.id == reservation_id).first()
        reservation.status = status
        self.session.commit()
        return reservation
    
    def get_confirmed_reservations(self) -> List:
        return self.session.query(Reservation).filter(Reservation.status == 'CONFIRMADA').options(
            joinedload(Reservation.table),
            joinedload(Reservation.user)
        ).all()
        
    def get_orders_by_reservation(self, reservation_id: int):
        return self.session.query(Reservation).filter(Reservation.id == reservation_id).options(joinedload(Reservation.orders)).first()