from infrastructure.database.models import User
from domain.repositories.user_repository import UserRepository

class UserSQLAlchemyRepository(UserRepository):
    def __init__(self, db_session):
        self.db_session = db_session
        
    def find_by_username(self, username: str) -> bool:
        return self.db_session.query(User).filter(User.username == username).first()
    
    def get_one(self, id: int):
        return self.db_session.query(User).filter(User.id == id).first()
    
    def find_all(self, username: str, password: str) -> bool:
        return super().find_all(username, password)
    
    def save(self, user):
        entity = User(**user)
        self.db_session.add(entity)
        self.db_session.commit()
        self.db_session.refresh(entity)
        return entity