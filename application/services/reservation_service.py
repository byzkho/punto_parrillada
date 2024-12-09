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
        reservation_data['reservation_time'] = self.format_reservation_time(reservation_data['reservation_time'])
        return self.reservation_repository.create(reservation_data)
    
    def format_reservation_time(self, reservation_time):
        date_time_str = reservation_time
        if '[' in date_time_str:
            date_time_str = date_time_str.split('[')[0]
        return parser.parse(date_time_str)

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
    
    def confirm_reservation(self, reservation_id):
        self.table_repository.update_status(reservation_id, 'OCUPADO')
        return self.reservation_repository.update_status_reservation(reservation_id, 'CONFIRMADA')
    
    def cancel_reservation(self, reservation_id, status):
        return self.reservation_repository.update_status_reservation(reservation_id, 'CANCELADA')
    
    def finalize_reservation(self, reservation_id, status):
        return self.reservation_repository.update_status_reservation(reservation_id, 'FINALIZADA')
    
    def get_confirmed_reservations(self):
        return self.reservation_repository.get_confirmed_reservations()
    
    def get_orders_by_reservation(self, reservation_id):
        return self.reservation_repository.get_orders_by_reservation(reservation_id)