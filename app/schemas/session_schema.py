from typing import Optional
from datetime import datetime
from pydantic import BaseModel

from app.schemas.table_schema import TableSchema


class SessionSchema(BaseModel):
    user_id: int
    table: TableSchema
    reservated_at: Optional[datetime] = None
    ocuppated_at: Optional[datetime] = None
    free_at: Optional[datetime] = None