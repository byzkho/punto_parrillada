from typing import Optional
from pydantic import BaseModel
from datetime import datetime
from infrastructure.database.models import UserRole

class UserBase(BaseModel):
    id: Optional[int]
    username: str
    email: str
    role: UserRole
    
    class Config:
        from_attributes = True

class TableBase(BaseModel):
    number: int
    status: str
    seats: int

class ReservationBase(BaseModel):
    table_id: int
    user_id: int
    date_time: datetime

class OrderBase(BaseModel):
    table_id: int
    items: str

class BillBase(BaseModel):
    order_id: int
    total_amount: float
    split: bool

