from pydantic import BaseModel
from datetime import datetime
from enum import Enum

class UserRole(str, Enum):
    ADMIN = "admin"
    RECEPCION = "recepcion"
    MESERO = "mesero"
    CAJERO = "cajero"

class UserBase(BaseModel):
    username: str
    role: UserRole

class TableBase(BaseModel):
    number: int
    status: str
    seats: int

class ReservationBase(BaseModel):
    table_id: int
    user_id: int
    date_time: datetime
    duration: float

class OrderBase(BaseModel):
    table_id: int
    items: str

class BillBase(BaseModel):
    order_id: int
    total_amount: float
    split: bool

