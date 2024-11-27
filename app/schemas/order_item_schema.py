from pydantic import BaseModel


class OrderItemSchema(BaseModel):
    id: int
    product: str