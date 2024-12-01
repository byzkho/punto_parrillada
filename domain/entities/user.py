from pydantic import BaseModel


class User(BaseModel):
    id: int
    username: str
    full_name: str
    email: str
    role: str
    
    def to_dict(self):
        return {
            "id": self.id,
            "username": self.username,
            "full_name": self.full_name,
            "email": self.email,
            "role": self.role
        }