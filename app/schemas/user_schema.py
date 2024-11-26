from pydantic import BaseModel

from domain.enum.user_role import UserRole


class UserSchema(BaseModel):
    id: int
    username: str
    full_name: str
    avatar: str | None
    email: str
    role: str