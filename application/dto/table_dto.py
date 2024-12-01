from pydantic import BaseModel
from application.dto.seat_dto import SeatDTO

class TableDTO(BaseModel):
    capacity: int