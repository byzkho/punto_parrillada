from typing import Optional
from fastapi_users import schemas


class UserRead(schemas.BaseUser[int]):
    role: str

class UserCreate(schemas.BaseUserCreate):
    role: Optional[str] = "user"

class UserUpdate(schemas.BaseUserUpdate):
    role: Optional[str] = None