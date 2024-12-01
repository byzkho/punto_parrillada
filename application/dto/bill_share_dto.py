from pydantic import BaseModel
from typing import Optional

class BillShareDTO(BaseModel):
    full_name: str
    amount: float