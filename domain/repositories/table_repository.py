from abc import ABC, abstractmethod
from typing import List

from domain.entities.table import Table


class TableRepository(ABC):
    @abstractmethod
    def get_all(self) -> List:
        pass
    
    @abstractmethod
    def get_one(self, id: int):
        pass

    @abstractmethod
    def create(self, table: Table):
        pass

    @abstractmethod
    def update(self, table: Table):
        pass

    @abstractmethod
    def delete(self, id: int):
        pass

    @abstractmethod
    def get_by_name(self, name: str):
        pass

    @abstractmethod
    def get_by_restaurant(self, restaurant_id: int) -> List:
        pass
    
    @abstractmethod
    def update_status(self, table_id: int, status: str):
        pass
    
    @abstractmethod
    def exists(self, table_id: int) -> bool:
        pass
    
    @abstractmethod
    def is_available(self, table_id: int) -> bool:
        pass
    
    @abstractmethod
    def get_seats_by_table(self, table_id: int):
        pass