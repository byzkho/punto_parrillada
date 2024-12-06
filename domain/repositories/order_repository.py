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
    
    @abstractmethod
    def update_ocuppated_at(self, reservation_id: int, status: str):
        pass
    
    @abstractmethod
    def create_order_item(self, order_id: int, product_id: int, seat_id: int, quantity: int):
        pass
    
    @abstractmethod
    def update_order_status(self, order_id: int, is_preparing: bool):
        pass
    
    @abstractmethod
    def get_not_prepared_orders(self):
        pass
    
    @abstractmethod
    def get_not_preparing_orders(self):
        pass
    
    @abstractmethod
    def get_orders_by_user(self, user_id: int):
        pass
    