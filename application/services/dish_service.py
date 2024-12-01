from application.utils.check_founded import check_none_decorator
from application.utils.convert_mapper import dto_to_dict_decorator
from domain.repositories.dish_repository import DishRepository


class DishService:
    def __init__(self, dish_repository: DishRepository):
        self.dish_repository = dish_repository

    def get_dishes(self):
        return self.dish_repository.get_all()

    @check_none_decorator
    def get_dish(self, dish_id):
        return self.dish_repository.get_by_id(dish_id)

    @dto_to_dict_decorator
    def create_dish(self, dish):
        return self.dish_repository.create(dish)

    def update_dish(self, dish_id, dish):
        return self.dish_repository.update(dish_id, dish)

    def get_by_menu(self, menu_id):
        return self.dish_repository.get_by_menu(menu_id)