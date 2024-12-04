# order_repository_impl.py
from domain.entities.reservation import Reservation
from domain.repositories.order_repository import OrderRepository
from infrastructure.database.models import Order, OrderItem, OrderStatus
from sqlalchemy.orm import Session, joinedload

class OrderRepositoryImpl(OrderRepository):
    def __init__(self, session: Session):
        self.session = session

    def get_all(self):
        return self.session.query(Order).options(joinedload(Order.order_items)).all()

    def get_one(self, id: int):
        return self.session.query(Order).filter(Order.id == id).options(joinedload(Order.order_items)).first()

    def create(self, order: dict):
        entity = Order(**order)
        self.session.add(entity)
        self.session.commit()
        self.session.refresh(entity)
        return entity.to_dict()

    def update(self, order: dict):
        existing_order = self.session.query(Order).filter(Order.id == order['id']).first()
        if existing_order:
            for key, value in order.items():
                setattr(existing_order, key, value)
            self.session.commit()
            self.session.refresh(existing_order)
            return existing_order.to_dict()
        return None

    def delete(self, order_id: int):
        order = self.session.query(Order).filter(Order.id == order_id).first()
        if order:
            self.session.delete(order)
            self.session.commit()
            return order.to_dict()
        return None

    def create_order_item(self, order_item: dict):
        entity = OrderItem(**order_item)
        self.session.add(entity)
        self.session.commit()
        self.session.refresh(entity)
        return entity.to_dict()

    def update_order_status(self, order_id: int, status: str):
        order = self.session.query(Order).filter(Order.id == order_id).first()
        order.status = status
        self.session.commit()
        return order.to_dict()

    def get_not_prepared_orders(self):
        return self.session.query(Order).filter(Order.status == OrderStatus.PREPARANDO).all()

    def get_not_preparing_orders(self):
        return self.session.query(Order).filter(Order.status == OrderStatus.PENDIENTE).all()

    def get_orders_by_user(self, user_id: int):
        return self.session.query(Order).join(Order.reservation).filter(Reservation.user_id == user_id).options(joinedload(Order.order_items)).all()
    
    def update_ocuppated_at(self, session_id: int, ocuppated_at: str):
        session = self.session.query(Reservation).filter(Reservation.id == session_id).first()
        session.ocuppated_at = ocuppated_at
        self.session.commit()
        return session.to_dict()