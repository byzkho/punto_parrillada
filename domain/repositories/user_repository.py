from abc import ABC, abstractmethod
from typing import Optional

from domain.entities.user import User

class UserRepository(ABC):
    @abstractmethod
    def find_by_username(self, username: str, password: str) -> Optional[User]:
        raise NotImplementedError
    
    @abstractmethod
    def find_all(self, username: str, password: str) -> bool:
        pass
    
    @abstractmethod
    def get_one(self, id: int):
        pass
    
    @abstractmethod
    def save(self, user):
        pass
    
    @abstractmethod
    def verify_already_exists(self, username: str, email: str) -> bool:
        pass