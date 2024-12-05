from domain.entities.reservation import Reservation
from domain.repositories.reservation_repository import ReservationRepository
from dateutil import parser

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
        table = self.table_repository.get_one(reservation.table_id)
        if int(reservation.quantity) > len(table.seats):
            raise Exception("La mesa no tiene suficientes asientos")
        self.table_repository.update_status(reservation.table_id, 'RESERVADA')
        reservation_data = reservation.__dict__
        date_time_str = reservation_data['reservation_time']
        if '[' in date_time_str:
            date_time_str = date_time_str.split('[')[0]
        
        reservation_data["reservation_time"] = parser.parse(date_time_str)
        return self.reservation_repository.create(reservation_data)

    def get_all(self):
        return self.reservation_repository.get_all()

    def get_one(self, reservation_id):
        return self.reservation_repository.get_one(reservation_id)

    def update(self, reservation):
        return self.reservation_repository.update(reservation)

    def delete(self, reservation_id):
        return self.reservation_repository.delete(reservation_id)
    
    def get_by_user(self, user_id):
        return self.reservation_repository.get_by_user(user_id)
    
    def get_confirmed_reservations_by_user(self, user_id):
        return self.reservation_repository.get_confirmed_reservations_by_user(user_id)
    
    def update_status_reservation(self, reservation_id, status):
        return self.reservation_repository.update_status_reservation(reservation_id, status)