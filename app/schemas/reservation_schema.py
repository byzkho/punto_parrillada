from datetime import datetime
from pydantic import BaseModel

from app.schemas.table_schema import TableSchema
from app.schemas.user_schema import UserSchema


class ReservationSchema(BaseModel):
    id: int
    table: TableSchema  # Incluir la relación con TableSchema
    user: UserSchema  # Incluir la relación con UserSchema
    reservation_time: datetime
    quantity: int