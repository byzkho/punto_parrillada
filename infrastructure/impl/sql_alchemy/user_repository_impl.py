from domain.enum.user_role import UserRole
from infrastructure.database.models import User
from domain.repositories.user_repository import UserRepository
from sqlalchemy.orm import Session

class UserSQLAlchemyRepository(UserRepository):
    def __init__(self, db_session: Session):
        self.db_session = db_session
        
    def find_by_username(self, username: str) -> bool:
        return self.db_session.query(User).filter(User.username == username).first()
    
    def get_one(self, id: int):
        return self.db_session.query(User).filter(User.id == id).first()
    
    def find_all(self) -> bool:
        return self.db_session.query(User).all()
    
    def save(self, user):
        if isinstance(user["role"], UserRole):
            user["role"] = user["role"].value   
        print(f"Role convertido en save: {user['role']} ({type(user['role'])})")
        entity = User(**user)
        self.db_session.add(entity)
        self.db_session.commit()
        self.db_session.refresh(entity)
        return entity
    
    def verify_already_exists(self, username: str, email: str) -> bool:
        return self.db_session.query(User).filter((User.username == username) | (User.email == email)).first() is not None