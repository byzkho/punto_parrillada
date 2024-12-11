from application.services.mail_service import MailService
from domain.entities.reservation import Reservation
from domain.repositories.reservation_repository import ReservationRepository
from dateutil import parser

from domain.repositories.table_repository import TableRepository
from domain.repositories.user_repository import UserRepository

class ReservationService:
    def __init__(self, reservation_repository: ReservationRepository, table_repository: TableRepository, mail_service: MailService, user_repository: UserRepository):
        self.reservation_repository = reservation_repository
        self.table_repository = table_repository
        self.mail_service = mail_service
        self.user_repository = user_repository

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
        reservation_created = self.reservation_repository.create(reservation_data)
        user = self.user_repository.get_one(reservation.user_id)
        reservation_info = {
            "user_name": user.full_name,
            "reservation_time": reservation_data['reservation_time'],
            "table_number": table.id,
            "quantity": reservation.quantity
        }
        
        self.send_reservation_email(user.email, reservation_info)
    
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
        reservation = self.reservation_repository.get_one(reservation_id)
        self.table_repository.update_status(reservation.table_id, 'OCUPADO')
        reservation_info = reservation.to_dict()
        self.send_confirmation_email(self.user_repository.get_one(reservation.user_id).email, reservation_info)
        return self.reservation_repository.update_status_reservation(reservation_id, 'CONFIRMADA')
    
    def cancel_reservation(self, reservation_id):
        reservation = self.reservation_repository.get_one(reservation_id)
        self.table_repository.update_status(reservation.table_id, 'LIBRE')
        return self.reservation_repository.update_status_reservation(reservation_id, 'CANCELADA')
    
    def finalize_reservation(self, reservation_id):
        reservation = self.reservation_repository.get_one(reservation_id)
        self.table_repository.update_status(reservation.table_id, 'LIBRE')
        return self.reservation_repository.update_status_reservation(reservation_id, 'FINALIZADA')
    
    def get_confirmed_reservations(self):
        return self.reservation_repository.get_confirmed_reservations()
    
    def get_orders_by_reservation(self, reservation_id):
        return self.reservation_repository.get_orders_by_reservation(reservation_id)
    
    def send_reservation_email(self, recipient: str, reservation_info: dict):
        subject = "Confirmación de Reserva"
        html_content = f"""
        <html>
        <head></head>
        <body>
            <h1>Hola {reservation_info['user_name']}</h1>
            <p>Gracias por tu reserva.</p>
            <p>Detalles de la reserva:</p>
            <ul>
                <li>Fecha y hora de la reserva: {reservation_info['reservation_time']}</li>
                <li>Mesa: {reservation_info['table_number']}</li>
                <li>Cantidad de personas: {reservation_info['quantity']}</li>
            </ul>
        </body>
        </html>
        """
        self.mail_service.send_mail(subject=subject, recipient=recipient, html_content=html_content)
        
    def send_confirmation_email(self, recipient: str, reservation_info: dict):
        # Convertir objetos de SQLAlchemy a diccionarios simples
        reservation_info['status'] = reservation_info['status']
        reservation_info['user'] = reservation_info['user']

        subject = "Reserva Confirmada"
        html_content = f"""
        <html>
        <head></head>
        <body>
            <h1>Hola {reservation_info['user']['full_name']}</h1>
            <p>Tu reserva ha sido confirmada.</p>
            <p>Detalles de la reserva:</p>
            <ul>
                <li>Fecha y hora de la reserva: {reservation_info['reservation_time']}</li>
                <li>Cantidad de personas: {reservation_info['quantity']}</li>
            </ul>
        </body>
        </html>
        """
        self.mail_service.send_mail(subject=subject, recipient=recipient, html_content=html_content)