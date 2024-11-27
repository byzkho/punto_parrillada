from domain.entities.reservation import Reservation
from domain.repositories.reservation_repository import ReservationRepository
from datetime import datetime

from domain.repositories.table_repository import TableRepository

class ReservationService:
    def __init__(self, reservation_repository: ReservationRepository, table_repository: TableRepository):
        self.reservation_repository = reservation_repository
        self.table_repository = table_repository

    def create(self, reservation: Reservation):
        if not self.table_repository.exists(reservation.table_id):
            raise Exception("La mesa no existe")
        if not self.table_repository.is_available(reservation.table_id):
            raise Exception("La mesa no está disponible")
        elif not self.table_repository.get_one(reservation.table_id).seats >= reservation.quantity:
            raise Exception("La mesa no tiene suficientes asientos")
        self.reservation_repository.create_user_table(reservation.table_id, reservation.user_id, datetime.now())
        self.table_repository.update_status(reservation.table_id, 'RESERVADA')
        reservation_data = reservation.__dict__
        reservation_data["date_time"] = datetime.strptime(reservation_data['date_time'], '%Y-%m-%dT%H:%M')
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