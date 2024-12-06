from fastapi import APIRouter, Depends

from application.dto.table_dto import TableDTO
from application.services.table_service import TableService
from infrastructure.providers.provider_module import get_table_service


router = APIRouter()

@router.get("/tables")
def get_tables(table_service: TableService = Depends(get_table_service)):
    return table_service.get_all_tables()

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