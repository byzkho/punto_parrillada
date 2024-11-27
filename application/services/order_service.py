from domain.entities.order import Order
from domain.repositories.order_repository import OrderRepository


class OrderService:
    def __init__(self, order_repository: OrderRepository):
        self.order_repository = order_repository

    def create_order(self, order: Order):
        self.order_repository.save(order)
        
    def get_all_orders(self):
        return self.order_repository.get_all()
    
    def get_order(self, order_id: int):
        return self.order_repository.get_one(order_id)
    
    def update_order(self, order: Order):
        self.order_repository.update(order)