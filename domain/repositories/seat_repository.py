from abc import ABC, abstractmethod
from typing import List

from domain.entities.seat import Seat


class SeatRepository(ABC):
    @abstractmethod
    def get_by_id(self, seat_id: int) -> Seat:
        pass

    @abstractmethod
    def get_all(self) -> List[Seat]:
        pass
    
    @abstractmethod
    def create(self, seat: Seat) -> Seat:
        pass
    
    @abstractmethod
    def get_by_table(self, table_id: int) -> List[Seat]:
        pass