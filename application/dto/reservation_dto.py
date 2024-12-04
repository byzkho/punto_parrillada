from typing import Optional
from pydantic import BaseModel


class ReservationDto(BaseModel):
    table_id: int
    user_id: Optional[int] = None
    reservation_time: str
    quantity: int