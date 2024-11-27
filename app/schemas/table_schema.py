from pydantic import BaseModel


class TableSchema(BaseModel):
    id: int
    number: int
    seats: int