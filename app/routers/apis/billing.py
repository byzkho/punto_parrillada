from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from application.dto.bill_dto import BillDTO
from application.services.bill_service import BillService
from infrastructure.database.database import get_db
from crud import billing as crud
from app.schemas.schemas import BillBase
from infrastructure.providers.provider_module import get_bill_service

router = APIRouter()

@router.post("/billings/")
def create_bill(bill: BillDTO, bill_service: BillService = Depends(get_bill_service)):
    return bill_service.create_bill(bill)

@router.get("/billings/{bill_id}")
def get_bill(bill_id: int, db: Session = Depends(get_db)):
    return crud.get_bill(db=db, bill_id=bill_id)
