from injector import Module, provider, singleton
from sqlalchemy.orm import Session

from application.services.table_service import TableService
from domain.repositories.table_repository import TableRepository
from infrastructure.impl.sql_alchemy.table_repository_impl import TableRepositoryImpl

class TableModule(Module):
    @singleton
    @provider
    def provide_table_repository(self, db_session: Session) -> TableRepository:
        return TableRepositoryImpl(db_session)
    
    @singleton
    @provider
    def provide_table_service(self, table_repository: TableRepository) -> TableService:
        return TableService(table_repository)