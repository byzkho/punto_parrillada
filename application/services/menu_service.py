from application.utils.check_founded import check_none_decorator
from application.utils.convert_mapper import dto_to_dict_decorator
from domain.entities.menu import Menu
from domain.repositories.menu_repository import MenuRepository


class MenuService:
    def __init__(self, menu_repository: MenuRepository):
        self.menu_repository = menu_repository

    def get_menu(self):
        return self.menu_repository.get_all()
    
    @check_none_decorator
    def get_menu_by_id(self, menu_id: int):
        return self.menu_repository.get_by_id(menu_id)
    
    @dto_to_dict_decorator
    def create_menu(self, menu: Menu):
        return self.menu_repository.create(menu)
    
    def update_menu(self, menu: Menu):
        return self.menu_repository.update(menu)
    
    def delete_menu(self, menu_id: int):
        return self.menu_repository.delete(menu_id)