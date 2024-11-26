from fastapi import APIRouter, Depends

from infrastructure.providers.provider_module import get_table_service


router = APIRouter()

@router.get("/")
def get_tables(table_service = Depends(get_table_service)):
    return table_service.get_all()

@router.get("/quantity")
def get_tables_by_quantity(quantity: int, table_service = Depends(get_table_service)):
    return table_service.get_by_range_of_seats(quantity)

@router.get("/{table_id}")
def get_table(table_id: int, table_service = Depends(get_table_service)):
    return table_service.get_by_id(table_id)

@router.post("/")
def create_table(table: dict, table_service = Depends(get_table_service)):
    return table_service.create(table)

@router.put("/")
def update_table(table: dict, table_service = Depends(get_table_service)):
    return table_service.update(table)

@router.post("/status")
def update_table_status(table_id: int, status: str, table_service = Depends(get_table_service)):
    return table_service.update_status(table_id, status)