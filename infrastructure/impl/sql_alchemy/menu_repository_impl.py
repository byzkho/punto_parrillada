from application.utils.convert_mapper import dict_to_model_decorator
from infrastructure.database.models import Category, Dish, Menu
from domain.repositories.menu_repository import MenuRepository
from sqlalchemy.orm import joinedload, Session

class MenuRepositoryImpl(MenuRepository):
    def __init__(self, session: Session):
        self.session = session

    def get_all(self):
        return self.session.query(Menu).join(Category, Menu.category_id == Category.id).options(joinedload(Menu.category)).all()

    def get_by_id(self, menu_id: int):
        return (
            self.session.query(Menu)
            .options(
                joinedload(Menu.category),  # Carga la categoría asociada
                joinedload(Menu.dishes)    # Carga los platos asociados
            )
            .filter(Menu.id == menu_id)
            .first()
        )

    @dict_to_model_decorator(Menu)
    def create(self, menu: Menu):
        self.session.add(menu)
        self.session.commit()
        return menu

    def update(self, menu: Menu, menu_id: int):
        menu_entity = self.session.query(Menu).filter(Menu.id == menu_id).first()
        menu_entity.name = menu.name
        menu_entity.category_id = menu.category_id
        self.session.commit()
        return menu_entity

    def delete(self, menu_id: int):
        menu = self.get_by_id(menu_id)
        self.session.delete(menu)
        self.session.commit()