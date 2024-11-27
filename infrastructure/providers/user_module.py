from injector import Module, provider, singleton
from application.services.user_service import UserService
from domain.repositories.user_repository import UserRepository
from sqlalchemy.orm import Session

from infrastructure.impl.sql_alchemy.user_repository_impl import UserSQLAlchemyRepository

class UserModule(Module):
    @singleton
    @provider
    def provide_user_repository(self, session: Session) -> UserRepository:
        return UserSQLAlchemyRepository(session)
    
    @singleton
    @provider
    def provide_user_service(self, repository: UserRepository) -> UserService:
        return UserService(repository)