from application.utils.check_founded import check_none_decorator
from application.utils.convert_mapper import dto_to_dict_decorator
from domain.repositories.category_repository import CategoryRepository

class CategoryService:
    def __init__(self, categoru_repository: CategoryRepository):
        self.category_repository = categoru_repository

    def get_all(self):
        return self.category_repository.get_all()

    @check_none_decorator
    def get_by_id(self, id):
        return self.category_repository.get_by_id(id)
    
    @dto_to_dict_decorator
    def create(self, category):
        return self.category_repository.create(category)

    def update(self, category):
        return self.category_repository.update(category)

    def delete(self, id):
        return self.category_repository.delete(id)