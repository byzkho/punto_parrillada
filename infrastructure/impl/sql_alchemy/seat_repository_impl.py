from typing import List
from domain.repositories.seat_repository import SeatRepository
from infrastructure.database.models import Seat


class SeatRepositoryImpl(SeatRepository):
    def __init__(self, session):
        self.session = session

    def get_by_id(self, seat_id: int) -> Seat:
        return self.session.query(Seat).filter(Seat.id == seat_id).first()

    def get_all(self) -> List[Seat]:
        return self.session.query(Seat).all()

    def create(self, seat) -> Seat:
        seat = Seat(**seat)
        self.session.add(seat)
        self.session.commit()
        return seat

    def get_by_table(self, table_id: int) -> List[Seat]:
        return self.session.query(Seat).filter(Seat.table_id == table_id).all()