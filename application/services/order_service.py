from domain.entities.order import Order
from domain.repositories.order_repository import OrderRepository
from datetime import datetime

class OrderService:
    def __init__(self, order_repository: OrderRepository):
        self.order_repository = order_repository

    def create_order(self, order: Order):
        order_data = order.model_dump(exclude={"order_items"})
        order_created = self.order_repository.create(order_data)
        for item in order.order_items:
            self.order_repository.create_order_item(order_created.id, item.product_id, item.seat_id, item.quantity)
        return order_created
        
    def get_all_orders(self):
        return self.order_repository.get_all()
    
    def get_order(self, order_id: int):
        return self.order_repository.get_one(order_id)
    
    def update_order(self, order: Order):
        self.order_repository.update(order)
        
    def update_is_preparing(self, order_id: int):
        return self.order_repository.update_order_status(order_id, 'PREPARANDO')
    
    def update_is_prepared(self, order_id: int):
        return self.order_repository.update_order_status(order_id, 'LISTO')
    
    def update_is_served(self, order_id: int):
        return self.order_repository.update_order_status(order_id, 'SERVIDO')
    
    def get_not_prepare_orders(self):
        return self.order_repository.get_not_prepared_orders()
    
    def get_not_preparing_orders(self):
        return self.order_repository.get_not_preparing_orders()
    
    def get_orders_by_user(self, user_id: int):
        return self.order_repository.get_orders_by_user(user_id)