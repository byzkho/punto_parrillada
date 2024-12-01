from pydantic import BaseModel


class Seat(BaseModel):
    id: int
    table_id: int