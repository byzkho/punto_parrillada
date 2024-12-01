from injector import Injector, Module, provider, singleton
from app.manager.cookie_manager import CookieManager
from application.services.bill_service import BillService
from application.services.category_service import CategoryService
from application.services.dish_service import DishService
from application.services.menu_service import MenuService
from application.services.order_service import OrderService
from application.services.reservation_service import ReservationService
from application.services.seat_service import SeatService
from application.services.table_service import TableService
from application.services.user_service import UserService
from domain.repositories.role_repository import RoleRepository
from domain.repositories.table_repository import TableRepository
from infrastructure.database.database import get_db
from application.services.auth_service import AuthService
from application.services.token_service import TokenService
from infrastructure.providers.auth_module import AuthModule
from sqlalchemy.orm import Session
from infrastructure.providers.bill_module import BillModule
from infrastructure.providers.category_module import CategoryModule
from infrastructure.providers.dish_module import DishModule
from infrastructure.providers.menu_module import MenuModule
from infrastructure.providers.order_module import OrderModule
from infrastructure.providers.reservation_module import ReservationModule
from infrastructure.providers.role_module import RoleModule
from infrastructure.providers.seat_module import SeatModule
from infrastructure.providers.table_module import TableModule
from infrastructure.providers.user_module import UserModule

class AppModule(Module):
    @singleton
    @provider
    def provide_db_session(self) -> Session:
        return next(get_db())
    
injector = Injector([
    AppModule, 
    AuthModule, 
    RoleModule, 
    TableModule, 
    ReservationModule, 
    OrderModule, 
    UserModule, 
    BillModule,
    MenuModule, 
    CategoryModule,
    DishModule,
    SeatModule])

def get_auth_service() -> AuthService:
    return injector.get(AuthService)

def get_token_service() -> TokenService:
    return injector.get(TokenService)

def get_role_service() -> RoleRepository:
    return injector.get(RoleRepository)

def get_table_service() -> TableService:
    return injector.get(TableService)

def get_reservation_service() -> ReservationService:
    return injector.get(ReservationService)

def get_cookie_manager():
    return injector.get(CookieManager)

def get_order_service() -> OrderService:
    return injector.get(OrderService)

def get_user_service() -> UserService:
    return injector.get(UserService)

def get_bill_service() -> BillService:
    return injector.get(BillService)

def get_menu_service() -> MenuService:
    return injector.get(MenuService)

def get_category_service() -> CategoryService:
    return injector.get(CategoryService)

def get_dish_service() -> DishService:
    return injector.get(DishService)

def get_seat_service() -> SeatService:
    return injector.get(SeatService)