from pydantic import BaseModel


class Dish(BaseModel):
    id: int
    name: str
    price: float
    description: str
    size: str
    menu_id: int