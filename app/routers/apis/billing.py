from fastapi import APIRouter, Depends, Request
from application.dto.bill_dto import BillDTO
from application.services.bill_service import BillService
from infrastructure.providers.provider_module import get_bill_service

router = APIRouter()

@router.post("/billings/")
def create_bill(bill: BillDTO, bill_service: BillService = Depends(get_bill_service)):
    return bill_service.create_bill(bill)


@router.get("/billings/")
def get_all_bill(bill_service: BillService = Depends(get_bill_service)):
    return bill_service.get_all_bills()

@router.get("/billings/auth/user")
def get_bill_by_user(request: Request, bill_service: BillService = Depends(get_bill_service)):
    return bill_service.get_bill_by_user(request.state.user.id)

@router.get("/billings/{bill_id}")
def get_bill(bill_id: int, bill_service: BillService = Depends(get_bill_service)):
    return bill_service.get_bill(bill_id)