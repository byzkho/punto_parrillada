from typing import Optional
from pydantic import BaseModel, Field, model_validator

from application.dto.bill_share_dto import BillShareDTO


class BillDTO(BaseModel):
    order_id: int
    split: Optional[int]