from pydantic import BaseModel


class Reservation(BaseModel):
    table_id: int
    user_id: int
    date_time: str
    quantity: int