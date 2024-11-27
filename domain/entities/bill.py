from pydantic import BaseModel


class Bill(BaseModel):
    id: int
    order_id: int
    total_amount: float
    split: bool