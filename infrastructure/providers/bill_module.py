from injector import Module, provider, singleton
from sqlalchemy.orm import Session

from application.services.bill_service import BillService
from domain.repositories.bill_repository import BillRepository
from domain.repositories.order_repository import OrderRepository
from domain.repositories.reservation_repository import ReservationRepository
from infrastructure.impl.sql_alchemy.bill_repository_impl import BillRepositoryImpl


class BillModule(Module):
    @singleton
    @provider
    def provide_bill_repository(self, session: Session) -> BillRepository:
        return BillRepositoryImpl(session)
    
    @singleton
    @provider
    def provide_bill_service(self, repository: BillRepository, order_repository: OrderRepository, ) -> BillService:
        return BillService(repository, order_repository)