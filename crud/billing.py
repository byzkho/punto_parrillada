from sqlalchemy.orm import Session
from app.config.database.models import Bill
from app.schemas.schemas import BillBase

def create_bill(db: Session, bill: BillBase):
    db_bill = Bill(**bill.model_dump())
    db.add(db_bill)
    db.commit()
    db.refresh(db_bill)
    return db_bill

def get_bill(db: Session, bill_id: int):
    return db.query(Bill).filter(Bill.id == bill_id).first()
