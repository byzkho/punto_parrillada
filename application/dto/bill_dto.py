from typing import Optional
from pydantic import BaseModel, Field, model_validator

from application.dto.bill_share_dto import BillShareDTO


class BillDTO(BaseModel):
    order_id: int
    total_amount: float
    split: bool
    shares: Optional[list[BillShareDTO]] = Field(default=None)
    
    @model_validator(mode="after")
    def validate_split_and_shares(cls, model):
        print(model)
        print("split: ", model.split)
        if model.split and not model.shares:
            raise ValueError("Debe proporcionar 'shares' cuando 'split' es True.")
        if not model.split and model.shares:
            raise ValueError("No debe proporcionar 'shares' cuando 'split' es False.")
        if model.split and model.shares:
            total_shared = sum(share.amount for share in model.shares)
            if total_shared != model.total_amount:
                raise ValueError("El total compartido no coincide con el total de la factura.")
        return model