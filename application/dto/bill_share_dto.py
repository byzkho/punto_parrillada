from pydantic import BaseModel
from typing import Optional

class BillShareDTO(BaseModel):
    bill_id: Optional[int] = None
    full_name: str
    amount: float