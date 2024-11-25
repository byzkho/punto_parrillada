from injector import Module, provider, singleton
from sqlalchemy.orm import Session
from application.services.role_service import RoleService
from domain.repositories.role_repository import RoleRepository
from infrastructure.impl.sql_alchemy.role_repository_impl import RoleRepositoryImpl


class RoleModule(Module):
    @singleton
    @provider
    def provide_role_repository(self, db_session: Session) -> RoleRepository:
        return RoleRepositoryImpl(db_session)
        
    @singleton
    @provider
    def provide_role_service(self, role_repository: RoleRepository) -> RoleService:
        return RoleService(role_repository)