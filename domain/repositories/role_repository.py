from abc import ABC, abstractmethod
from typing import List


class RoleRepository(ABC):
    @abstractmethod
    def get_all(self) -> List:
        pass
    
    @abstractmethod
    def get_one(self, id: int):
        pass