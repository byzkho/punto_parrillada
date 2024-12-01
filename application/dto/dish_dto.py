from pydantic import BaseModel


class DishDTO(BaseModel):
    menu_id: int
    name: str
    price: float
    description: str
    size: str