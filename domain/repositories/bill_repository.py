from abc import ABC, abstractmethod
from typing import List

from infrastructure.database.models import Bill


class BillRepository(ABC):
    @abstractmethod
    def get_all(self) -> List:
        pass
    
    @abstractmethod
    def get_one(self, id: int):
        pass

    @abstractmethod
    def create(self, bill: Bill):
        pass
    
    @abstractmethod
    def get_by_order(self, order_id: int) -> List:
        pass
    
    @abstractmethod
    def create_share(self, share: dict):
        pass