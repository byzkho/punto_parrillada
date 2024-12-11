from injector import Module, provider, singleton
from application.services.mail_service import MailService
from application.services.reservation_service import ReservationService
from domain.repositories.reservation_repository import ReservationRepository
from sqlalchemy.orm import Session

from domain.repositories.table_repository import TableRepository
from domain.repositories.user_repository import UserRepository
from infrastructure.impl.sql_alchemy.reservation_repository_impl import ReservationRepositoryImpl

class ReservationModule(Module):
    @singleton
    @provider
    def provide_reservation_repository(self, db_session: Session) -> ReservationRepository:
        return ReservationRepositoryImpl(db_session)
    
    @singleton
    @provider
    def provide_reservation_service(self, reservation_repository: ReservationRepository, table_repository: TableRepository, mail_service: MailService, user_repository: UserRepository) -> ReservationService:
        return ReservationService(reservation_repository, table_repository, mail_service, user_repository)