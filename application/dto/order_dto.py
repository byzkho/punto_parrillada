from typing import Optional, List
from pydantic import BaseModel

from application.dto.order_items_dto import OrderItemsDTO


class OrderDto(BaseModel):
    reservation_id: Optional[int] = None
    waiter_id: Optional[int] = None
    order_items: Optional[List[OrderItemsDTO]] = None