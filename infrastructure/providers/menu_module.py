from injector import Module, provider, singleton
from sqlalchemy.orm import Session
from application.services.menu_service import MenuService
from domain.repositories.menu_repository import MenuRepository
from infrastructure.impl.sql_alchemy.menu_repository_impl import MenuRepositoryImpl


class MenuModule(Module):
    @singleton
    @provider
    def provide_menu_repository(self, session: Session) -> MenuRepository:
        return MenuRepositoryImpl(session)
    
    @singleton
    @provider
    def provide_menu_service(self, repository: MenuRepository) -> MenuService:
        return MenuService(repository)