from abc import ABC, abstractmethod
from typing import List

from infrastructure.database.models import Reservation


class ReservationRepository(ABC):
    @abstractmethod
    def get_all(self) -> List:
        pass
    
    @abstractmethod
    def get_one(self, id: int):
        pass

    @abstractmethod
    def create(self, reservation: Reservation):
        pass

    @abstractmethod
    def update(self, reservation: Reservation):
        pass

    @abstractmethod
    def delete(self, id: int):
        pass

    @abstractmethod
    def get_by_user(self, user_id: int) -> List:
        pass
    
    @abstractmethod
    def create_user_table(self, user_table):
        pass
    
    @abstractmethod
    def update_status_reservation(self, reservation_id: int, status: str):
        pass
    
    @abstractmethod
    def get_confirmed_reservations_by_user(self, user_id: int) -> List:
        pass
    
    @abstractmethod
    def get_confirmed_reservations(self) -> List:
        pass
    
    
    @abstractmethod
    def get_orders_by_reservation(self, reservation_id: int):
        pass