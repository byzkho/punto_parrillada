from domain.repositories.table_repository import TableRepository
from infrastructure.database.models import Table, TableStatus


class TableRepositoryImpl(TableRepository):
    def __init__(self, session):
        self.session = session

    def get_all(self):
        return self.session.query(Table).all()

    def get_one(self, id: int):
        return self.session.query(Table).filter(Table.id == id).first()

    def create(self, table: Table):
        self.session.add(table)
        self.session.commit()

    def update(self, table: Table):
        self.session.add(table)
        self.session.commit()

    def delete(self, id: int):
        table = self.session.query(Table).filter(Table.id == id).first()
        self.session.delete(table)
        self.session.commit()

    def get_by_name(self, name: str):
        return self.session.query(Table).filter(Table.name == name).first()

    def get_by_restaurant(self, restaurant_id: int):
        return self.session.query(Table).filter(Table.restaurant_id == restaurant_id).all()
    
    def get_by_range_of_seats(self, quantity_of_seats: int):
        return self.session.query(Table).filter(Table.seats >= quantity_of_seats).filter(Table.status == TableStatus.LIBRE).all()
    
    def update_status(self, table_id: int, status: str):
        table = self.session.query(Table).filter(Table.id == table_id).first()
        table.status = status
        self.session.commit()
        return table
    
    def exists(self, table_id: int) -> bool:
        return self.session.query(Table).filter(Table.id == table_id).count() > 0
    
    def is_available(self, table_id: int) -> bool:
        return self.session.query(Table).filter(Table.id == table_id).filter(Table.status == TableStatus.LIBRE).count() > 0