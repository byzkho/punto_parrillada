from injector import Module, provider, singleton
from application.services.dish_service import DishService
from domain.repositories.dish_repository import DishRepository
from infrastructure.impl.sql_alchemy.dish_repository_impl import DishRepositoryImpl
from sqlalchemy.orm import Session

class DishModule(Module):
    @singleton
    @provider
    def provide_dish_repository(self, session: Session) -> DishRepository:
        return DishRepositoryImpl(session)
    
    @singleton
    @provider
    def provide_dish_service(self, dish_repository: DishRepository) -> DishService:
        return DishService(dish_repository)