from abc import ABC, abstractmethod
from typing import List

from domain.entities.menu import Menu


class MenuRepository(ABC):
    @abstractmethod
    def get_all(self) -> List[Menu]:
        pass

    @abstractmethod
    def get_by_id(self, menu_id: int) -> Menu:
        pass

    @abstractmethod
    def create(self, menu: Menu) -> Menu:
        pass

    @abstractmethod
    def update(self, menu: Menu, id: int) -> Menu:
        pass

    @abstractmethod
    def delete(self, menu_id: int) -> None:
        pass