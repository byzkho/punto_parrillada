from pydantic import BaseModel


class User(BaseModel):
    id: int
    username: str
    full_name: str
    email: str
    role: str
    avatar: str