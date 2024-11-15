from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database import get_db
from crud import billing as crud
from app.schemas import BillBase

router = APIRouter()

@router.post("/billing/")
def create_bill(bill: BillBase, db: Session = Depends(get_db)):
    return crud.create_bill(db=db, bill=bill)

@router.get("/billing/{bill_id}")
def get_bill(bill_id: int, db: Session = Depends(get_db)):
    return crud.get_bill(db=db, bill_id=bill_id)
