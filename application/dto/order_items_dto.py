from typing import Optional
from pydantic import BaseModel


class OrderItemsDTO(BaseModel):
    order_id: Optional[int] = None
    seat_id: int
    product_id: int
    quantity: int