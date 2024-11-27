from injector import Module, provider, singleton
from sqlalchemy.orm import Session
from application.services.order_service import OrderService
from domain.repositories.order_repository import OrderRepository
from infrastructure.impl.sql_alchemy.order_repository_impl import OrderRepositoryImpl


class OrderModule(Module):
    @singleton
    @provider
    def provide_order_repository(self, session: Session) -> OrderRepository:
        return OrderRepositoryImpl(session)
    
    @singleton
    @provider
    def provide_order_service(self, order_repository: OrderRepository) -> OrderService:
        return OrderService(order_repository)