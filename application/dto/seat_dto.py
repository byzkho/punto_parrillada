from pydantic import BaseModel


class SeatDTO(BaseModel):
    number: int