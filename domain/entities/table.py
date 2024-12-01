from pydantic import BaseModel


class Table(BaseModel):
    id: int
    status: str
    capacity: int