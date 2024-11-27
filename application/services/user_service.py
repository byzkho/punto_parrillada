from domain.repositories.user_repository import UserRepository


class UserService:
    def __init__(self, user_repository: UserRepository):
        self.user_repository = user_repository

    def get_user(self, user_id):
        return self.user_repository.get_one(user_id)

    def get_users(self):
        return self.user_repository.find_all()