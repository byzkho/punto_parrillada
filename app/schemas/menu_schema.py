from pydantic import BaseModel

from app.schemas.category_schema import CategorySchema


class MenuSchema(BaseModel):
    id: int
    name: str
    category: CategorySchema