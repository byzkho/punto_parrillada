from injector import Module, provider, singleton
from application.services.seat_service import SeatService
from domain.repositories.seat_repository import SeatRepository
from infrastructure.impl.sql_alchemy.seat_repository_impl import SeatRepositoryImpl
from sqlalchemy.orm import Session

class SeatModule(Module):
    @singleton
    @provider
    def provide_seat_repository(self, session: Session) -> SeatRepository:
        return SeatRepositoryImpl(session)
    
    @singleton
    @provider
    def provide_seat_service(self, seat_repository: SeatRepository) -> SeatService:
        return SeatService(seat_repository)