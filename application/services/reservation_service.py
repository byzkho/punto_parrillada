from domain.entities.reservation import Reservation
from domain.repositories.reservation_repository import ReservationRepository
from datetime import datetime

from domain.repositories.table_repository import TableRepository

class ReservationService:
    def __init__(self, reservation_repository: ReservationRepository, table_repository: TableRepository):
        self.reservation_repository = reservation_repository
        self.table_repository = table_repository

    def create(self, reservation: Reservation):
        self.table_repository.update_status(reservation.table_id, 'RESERVADA')
        reservation_data = reservation.__dict__
        reservation_data["date_time"] = datetime.strptime(reservation_data['date_time'], '%Y-%m-%d')
        return self.reservation_repository.create(reservation_data)

    def get_all(self):
        return self.reservation_repository.get_all()

    def get_one(self, reservation_id):
        return self.reservation_repository.get_by_id(reservation_id)

    def update(self, reservation):
        return self.reservation_repository.update(reservation)

    def delete(self, reservation_id):
        return self.reservation_repository.delete(reservation_id)
    
    def get_by_user(self, user_id):
        return self.reservation_repository.get_by_user(user_id)