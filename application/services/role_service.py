class RoleService:
    def __init__(self, role_repository):
        self.role_repository = role_repository

    def get_all(self):
        return self.role_repository.get_all()
    
    def get_one(self, id: int):
        return self.role_repository.get_one(id)