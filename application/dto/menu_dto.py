from pydantic import BaseModel


class MenuDTO(BaseModel):
    name: str
    category_id: int