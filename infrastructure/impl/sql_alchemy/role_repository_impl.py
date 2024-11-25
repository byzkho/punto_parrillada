from domain.repositories.role_repository import RoleRepository
from infrastructure.database.models import UserRole


class RoleRepositoryImpl(RoleRepository):
    def __init__(self, session):
        self.session = session

    def get_all(self):
        return [{"key": role.name, "value": role.value} for role in UserRole]
    
    def get_one(self, id: int) -> UserRole:
        return self.session.query(UserRole).filter(UserRole.id == id).first()