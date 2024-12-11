from injector import Module, provider, singleton
from sqlalchemy.orm import Session

from application.services.bill_service import BillService
from application.services.reservation_service import ReservationService
from domain.repositories.bill_repository import BillRepository
from domain.repositories.order_repository import OrderRepository
from domain.repositories.reservation_repository import ReservationRepository
from domain.repositories.table_repository import TableRepository
from infrastructure.impl.sql_alchemy.bill_repository_impl import BillRepositoryImpl


class BillModule(Module):
    @singleton
    @provider
    def provide_bill_repository(self, session: Session) -> BillRepository:
        return BillRepositoryImpl(session)
    
    @singleton
    @provider
    def provide_bill_service(self, repository: BillRepository, order_repository: OrderRepository, table_repository: TableRepository, reservation_service: ReservationService) -> BillService:
        return BillService(repository, order_repository, table_repository, reservation_service)