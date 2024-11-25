from injector import Module, provider, singleton
from sqlalchemy.orm import Session
from domain.repositories.token_repository import TokenRepository
from domain.repositories.user_repository import UserRepository
from infrastructure.impl.sql_alchemy.token_repository_impl import TokenRepositoryImpl
from infrastructure.impl.sql_alchemy.user_repository_impl import UserSQLAlchemyRepository


class AuthModule(Module):
    @singleton
    @provider
    def provide_user_repository(self, db_session: Session) -> UserRepository:
        return UserSQLAlchemyRepository(db_session)

    @singleton
    @provider
    def provide_token_repository(self, db_session: Session) -> TokenRepository:
        return TokenRepositoryImpl(db_session)