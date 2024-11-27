from domain.repositories.order_repository import OrderRepository
from infrastructure.database.models import Order, OrderItem, OrderStatus, Session as OrderSession
from sqlalchemy.orm import Session, joinedload

class OrderRepositoryImpl(OrderRepository):
    def __init__(self, session: Session):
        self.session = session

    def get_all(self):
        return self.session.query(Order).options(joinedload(Order.session)).all()

    def get_one(self, id):
        return self.session.query(Order).filter(Order.id == id).first()

    def create(self, order):
        entity = Order(**order)
        self.session.add(entity)
        self.session.commit()
        self.session.refresh(entity)
        entity = self.session.query(Order).options(joinedload(Order.session).joinedload(OrderSession.table)).filter_by(id=entity.id).first()
        return entity

    def update(self, order):
        self.session.add(order)
        self.session.commit()
        return order
    
    def update_ocuppated_at(self, session_id: int, ocuppated_at: str):
        session_table = self.session.query(OrderSession).filter(OrderSession.id == session_id).first()
        session_table.ocuppated_at = ocuppated_at
        self.session.commit()
        return session_table
    
    def create_order_item(self, order_id: int, product: str):
        entity = OrderItem(order_id=order_id, product=product)
        self.session.add(entity)
        self.session.commit()
        return entity
    
    def update_order_status(self, order_id: int, status: str):
        order = self.session.query(Order).filter(Order.id == order_id).first()
        order.status = status
        self.session.commit()
        return order
    
    def get_not_prepared_orders(self):
        return self.session.query(Order).filter(Order.status == OrderStatus.PREPARANDO).all()
    
    def get_not_preparing_orders(self):
        return self.session.query(Order).filter(Order.status == OrderStatus.PENDIENTE).all()
    
    def get_orders_by_user(self, user_id: int):
        return self.session.query(Order).join(Order.session).filter(OrderSession.user_id == user_id).options(joinedload(Order.session), joinedload(Order.order_items)).all()