from typing import List
from domain.entities.user import User
from domain.repositories.bill_repository import BillRepository
from sqlalchemy.orm import Session, joinedload

from infrastructure.database.models import Bill, BillShare, Order, UserReservation as OrderSession

class BillRepositoryImpl(BillRepository):
    def __init__(self, session: Session):
        self.session = session

    def get_all(self) -> List[Bill]:
        return self.session.query(Bill).all()

    def get_one(self, bill_id: int) -> Bill:
        return (
        self.session.query(Bill)
        .join(Order, Bill.order_id == Order.id)
        .join(OrderSession, Order.session_id == OrderSession.id)
        .join(User, OrderSession.user_id == User.id)
        .filter(Bill.id == bill_id)
        .options(
            joinedload(Bill.order).joinedload(Order.session).joinedload(OrderSession.user)
        )
        .first()
    )

    def create(self, bill: Bill) -> Bill:
        entity = Bill(**bill)
        self.session.add(entity)
        self.session.commit()
        self.session.refresh(entity)
        return entity

    def get_by_order(self, order_id: int) -> List:
        return self.session.query(Bill).filter(Bill.order_id == order_id).first()
    
    def create_share(self, share: dict):
        entity = BillShare(**share)
        self.session.add(entity)
        self.session.commit()
        self.session.refresh(entity)
        return entity
    
    def get_bill_by_user(self, user_id: int):
        return (
            self.session.query(Bill)
            .join(Order, Bill.order_id == Order.id)
            .join(OrderSession, Order.session_id == OrderSession.id)
            .filter(OrderSession.user_id == user_id)
            .options(joinedload(Bill.order).joinedload(Order.session))
            .all()
        )
        
    def get_bill_by_order(self, order_id):
        return self.session.query(Bill).filter(Bill.order_id == order_id).first()