from injector import Module, provider, singleton
from application.services.category_service import CategoryService
from domain.repositories.category_repository import CategoryRepository
from sqlalchemy.orm import Session
from infrastructure.impl.sql_alchemy.category_repository_impl import CategoryRepositoryImpl


class CategoryModule(Module):
    @singleton
    @provider
    def provide_category_repository(self, session: Session) -> CategoryRepository:
        return CategoryRepositoryImpl(session)
    
    @singleton
    @provider
    def provide_category_service(self, repository: CategoryRepository) -> CategoryService:
        return CategoryService(repository)