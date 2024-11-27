from pydantic import BaseModel


class OrderDto(BaseModel):
    session_id: int
    items: list