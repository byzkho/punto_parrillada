from typing import Optional
from fastapi import APIRouter, Depends, Query, Request

from application.dto.table_dto import TableDTO
from application.services.table_service import TableService
from infrastructure.providers.provider_module import get_table_service


router = APIRouter()

@router.get("/tables")
def get_tables(status: Optional[str] = Query(None), quantity: Optional[str] = Query(None),  table_service: TableService = Depends(get_table_service)):
    return table_service.get_by_filter(quantity=quantity, status=status)

@router.get("/tables/{table_id}")
def get_table(table_id: int, table_service: TableService = Depends(get_table_service)):
    return table_service.get_table(table_id)

@router.post("/tables")
def create_table(table: TableDTO, table_service: TableService = Depends(get_table_service)):
    table_service.create_table(table)
    return {"message": "Table created successfully"}
    
@router.put("/tables")
def update_table(table: dict, table_service = Depends(get_table_service)):
    return table_service.update(table)

@router.post("/status")
def update_table_status(table_id: int, status: str, table_service = Depends(get_table_service)):
    return table_service.update_status(table_id, status)

@router.get("/seats/table/{id}")
def get_seats_by_table(id: int, table_service = Depends(get_table_service)):
    return table_service.get_seats_by_table(id)

@router.get("/tables/status/{status}")
def get_table_by_status(status: str, table_service = Depends(get_table_service)):
    return table_service.get_table_by_status(status)