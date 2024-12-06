from typing import List
from application.utils.convert_mapper import dto_to_dict_decorator
from domain.repositories.seat_repository import SeatRepository
from domain.repositories.table_repository import TableRepository
from domain.entities.table import Table


class TableService:
    def __init__(self, table_repository: TableRepository, seat_repository: SeatRepository):
        self.table_repository = table_repository
        self.seat_repository = seat_repository

    def get_table(self, table_id: int) -> Table:
        return self.table_repository.get_one(table_id)
    
    def get_all_tables(self) -> List[Table]:
        return self.table_repository.get_all()
    
    @dto_to_dict_decorator
    def create_table(self, table: Table):
        created_table: Table = self.table_repository.create(table)
        self.create_seats_by_capacity(created_table.id, created_table.capacity)
        return table
        
    def update_table(self, table: Table):
        self.table_repository.update_table(table)
        
    def get_by_range_of_seats(self, quantity: int) -> List[Table]:
        return self.table_repository.get_by_range_of_seats(quantity)
    
    def update_status(self, table_id: int, status: str):
        self.table_repository.update_status(table_id, status)
    
    
    def create_seats_by_capacity(self, table_id: int, capacity: int):
        for i in range(capacity):
            self.seat_repository.create({
                "table_id": table_id,
                "number": i + 1    
            })
            
    def get_seats_by_table(self, table_id: int):
        return self.table_repository.get_seats_by_table(table_id)