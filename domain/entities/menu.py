from pydantic import BaseModel

class Menu(BaseModel):
    id: int
    name: str
    category_id: int