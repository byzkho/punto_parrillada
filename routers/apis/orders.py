from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from infrastructure.database.database import get_db
from crud import orders as crud
from app.schemas.schemas import OrderBase

router = APIRouter()

@router.post("/orders/")
def create_order(order: OrderBase, db: Session = Depends(get_db)):
    return crud.create_order(db=db, order=order)

@router.get("/orders/{order_id}")
def get_order(order_id: int, db: Session = Depends(get_db)):
    return crud.get_order(db=db, order_id=order_id)

@router.put("/orders/{order_id}/status")
def update_order_status(order_id: int, status: bool, db: Session = Depends(get_db)):
    return crud.update_order_status(db=db, order_id=order_id, status=status)
