from abc import ABC, abstractmethod
from typing import List

from domain.entities.category import Category


class CategoryRepository(ABC):
    @abstractmethod
    def get_all(self) -> List[Category]:
        pass

    @abstractmethod
    def get_by_id(self, category_id: int) -> Category:
        pass

    @abstractmethod
    def create(self, category: Category) -> Category:
        pass

    @abstractmethod
    def update(self, category_id: int, data) -> Category:
        pass

    @abstractmethod
    def delete(self, category_id: int) -> None:
        pass