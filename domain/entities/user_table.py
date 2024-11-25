from typing import Optional
from pydantic import BaseModel


class UserTable(BaseModel):
    user_id: int
    table_id: int
    reservated_at: Optional[str] = None
    ocuppated_at: Optional[str] = None
    free_at: Optional[str] = None