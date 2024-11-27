from domain.entities.order import Order
from domain.repositories.order_repository import OrderRepository


class OrderRepositoryImpl(OrderRepository):
    def __init__(self, session):
        self.session = session

    def get_all(self):
        return self.session.query(Order).all()

    def get_one(self, id):
        return self.session.query(Order).filter(Order.id == id).first()

    def create(self, order):
        self.session.add(order)
        self.session.commit()
        return order

    def update(self, order):
        self.session.add(order)
        self.session.commit()
        return order