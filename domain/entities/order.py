from pydantic import BaseModel


class Order(BaseModel):
    id: int
    session_id: int
    items: str
    status: bool