from domain.repositories.dish_repository import DishRepository
from infrastructure.database.models import Dish
from application.utils.convert_mapper import dict_to_model_decorator

class DishRepositoryImpl(DishRepository):
    def __init__(self, db_session):
        self.db_session = db_session

    def get_all(self):
        return self.db_session.query(Dish).all()

    def get_by_id(self, id: int):
        return self.db_session.query(Dish).filter(Dish.id == id).first()

    dict_to_model_decorator(Dish)
    def create(self, dish):
        dish_entity = Dish(**dish)
        self.db_session.add(dish_entity)
        self.db_session.commit()
        return dish_entity

    def update(self, dish):
        self.db_session.add(dish)
        self.db_session.commit()

    def delete(self, id: int):
        dish = self.db_session.query(Dish).filter(Dish.id == id).first()
        self.db_session.delete(dish)
        self.db_session.commit()
        
    def get_by_menu(self, menu_id):
        return self.db_session.query(Dish).filter(Dish.menu_id == menu_id).all()

    