from abc import ABC, abstractmethod
from typing import List

from domain.entities.order import Order


class OrderRepository(ABC):
    @abstractmethod
    def get_all(self) -> List:
        pass
    
    @abstractmethod
    def get_one(self, id: int):
        pass

    @abstractmethod
    def create(self, order: Order):
        pass

    @abstractmethod
    def update(self, order: Order):
        pass