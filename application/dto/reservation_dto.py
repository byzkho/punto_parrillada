from typing import Optional
from pydantic import BaseModel


class ReservationDto(BaseModel):
    table_id: int
    user_id: Optional[int] = None
    date_time: str
    quantity: int