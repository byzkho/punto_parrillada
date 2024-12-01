from abc import ABC, abstractmethod


class DishRepository(ABC):
    @abstractmethod
    def get_all(self):
        pass

    @abstractmethod
    def get_by_id(self, dish_id):
        pass

    @abstractmethod
    def create(self, dish):
        pass

    @abstractmethod
    def update(self, dish_id, dish):
        pass

    @abstractmethod
    def delete(self, dish_id):
        pass
    
    @abstractmethod
    def get_by_menu(self, menu_id):
        pass