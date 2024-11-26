from injector import Injector, Module, provider, singleton
from app.manager.cookie_manager import CookieManager
from application.services.reservation_service import ReservationService
from domain.repositories.reservation_repository import ReservationRepository
from domain.repositories.role_repository import RoleRepository
from domain.repositories.table_repository import TableRepository
from infrastructure.database.database import get_db
from application.services.auth_service import AuthService
from application.services.token_service import TokenService
from domain.repositories.user_repository import UserRepository
from infrastructure.providers.auth_module import AuthModule
from sqlalchemy.orm import Session
from infrastructure.providers.reservation_module import ReservationModule
from infrastructure.providers.role_module import RoleModule
from infrastructure.providers.table_module import TableModule

class AppModule(Module):
    @singleton
    @provider
    def provide_db_session(self) -> Session:
        return next(get_db())
    
injector = Injector([AppModule, AuthModule, RoleModule, TableModule, ReservationModule])

def get_auth_service() -> AuthService:
    return injector.get(AuthService)

def get_token_service() -> TokenService:
    return injector.get(TokenService)

def get_user_service() -> UserRepository:
    return injector.get(UserRepository)

def get_role_service() -> RoleRepository:
    return injector.get(RoleRepository)

def get_table_service() -> TableRepository:
    return injector.get(TableRepository)

def get_reservation_service() -> ReservationService:
    return injector.get(ReservationService)

def get_cookie_manager():
    return injector.get(CookieManager)