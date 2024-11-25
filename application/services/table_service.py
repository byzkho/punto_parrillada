from typing import List
from domain.repositories.table_repository import TableRepository
from domain.entities.table import Table


class TableService:
    def __init__(self, table_repository: TableRepository):
        self.table_repository = table_repository

    def get_table(self, table_id: int) -> Table:
        return self.table_repository.get_table(table_id)
    
    def get_all_tables(self) -> List[Table]:
        
        return self.table_repository.get_all_tables()
    
    def create_table(self, table: Table):
        self.table_repository.create_table(table)
        
    def update_table(self, table: Table):
        self.table_repository.update_table(table)
        
    def get_by_range_of_seats(self, quantity: int) -> List[Table]:
        return self.table_repository.get_by_range_of_seats(quantity)
    
    def update_status(self, table_id: int, status: str):
        self.table_repository.update_status(table_id, status)