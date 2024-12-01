from application.utils.convert_mapper import dict_to_model_decorator
from domain.repositories.category_repository import CategoryRepository
from infrastructure.database.models import Category
from sqlalchemy.orm import Session

class CategoryRepositoryImpl(CategoryRepository):
    def __init__(self, session: Session):
        self.session = session

    def get_all(self):
        return self.session.query(Category).all()

    def get_by_id(self, category_id: int):
        return self.session.query(Category).filter(Category.id == category_id).first()

    @dict_to_model_decorator(Category)
    def create(self, category):
        self.session.add(category)
        self.session.commit()
        return category

    def update(self, category):
        self.session.add(category)
        self.session.commit()
        return category

    def delete(self, category_id: int):
        category = self.get_by_id(category_id)
        self.session.delete(category)
        self.session.commit()
        return None