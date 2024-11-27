from pydantic import BaseModel

from app.schemas.order_item_schema import OrderItemSchema
from app.schemas.session_schema import SessionSchema
from app.schemas.table_schema import TableSchema
from infrastructure.database.models import OrderStatus


class OrderSchema(BaseModel):
    id: int
    status: OrderStatus
    order_items: list[OrderItemSchema]
    session: SessionSchema