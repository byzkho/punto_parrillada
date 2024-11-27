from typing import List
from domain.repositories.bill_repository import BillRepository
from sqlalchemy.orm import Session

from infrastructure.database.models import Bill, BillShare

class BillRepositoryImpl(BillRepository):
    def __init__(self, session: Session):
        self.session = session

    def get_all(self) -> List[Bill]:
        return self.session.query(Bill).all()

    def get_one(self, bill_id: int) -> Bill:
        return self.session.query(Bill).filter(Bill.id == bill_id).one()

    def create(self, bill: Bill) -> Bill:
        entity = Bill(**bill)
        self.session.add(entity)
        self.session.commit()
        self.session.refresh(entity)
        return entity

    def get_by_order(self, order_id: int) -> List:
        return self.session.query(Bill).filter(Bill.order_id == order_id).all()
    
    def create_share(self, share: dict):
        entity = BillShare(**share)
        self.session.add(entity)
        self.session.commit()
        self.session.refresh(entity)
        return entity