from typing import List
from domain.repositories.reservation_repository import ReservationRepository
from infrastructure.database.models import Reservation, Session
from sqlalchemy.orm import joinedload

class ReservationRepositoryImpl(ReservationRepository):
    def __init__(self, session):
        self.session = session

    def create(self, reservation: Reservation):
        entity = Reservation(**reservation)
        self.session.add(entity)
        self.session.commit()
        return reservation

    def get_one(self, reservation_id: int) -> Reservation:
        return self.session.query(Reservation).filter_by(id=reservation_id).first()

    def get_all(self) -> List[Reservation]:
        return self.session.query(Reservation).all()

    def update(self, reservation: Reservation):
        self.session.commit()

    def delete(self, reservation: Reservation):
        self.session.delete(reservation)
        self.session.commit()
        
    def get_by_user(self, user_id: int) -> List[Reservation]:
        return self.session.query(Reservation).filter_by(user_id=user_id).options(joinedload(Reservation.table), joinedload(Reservation.user)).all()
    
    def create_user_table(self, table_id: int, user_id: int, reservated_at: str):
        user_table = Session(user_id=user_id, table_id=table_id, reservated_at=reservated_at)
        self.session.add(user_table)
        self.session.commit()
        return user_table