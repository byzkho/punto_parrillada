from fastapi import APIRouter, Depends

from application.dto.category_dto import CategoryDTO
from application.services.category_service import CategoryService
from infrastructure.providers.provider_module import get_category_service


router = APIRouter()

@router.get("/categories/")
async def get_all_categories(category_service: CategoryService = Depends(get_category_service)):
    return category_service.get_all()

@router.get("/categories/{category_id}")
async def get_category(category_id: str, category_service: CategoryService = Depends(get_category_service)):
    try:
        return category_service.get_by_id(category_id)
    except Exception as e:
        return {"message": str(e.detail["msg"])}

@router.post("/categories/")
async def create_category(category_dto: CategoryDTO, category_service: CategoryService = Depends(get_category_service)):
    category_service.create(category_dto)
    return {"message": "Category created successfully"}

@router.put("/categories/{category_id}")
async def update_category(category_id: int, category: CategoryDTO, category_service: CategoryService = Depends(get_category_service)):
    return category_service.update(category, category_id)

@router.delete("/categories/{category_id}")
async def delete_category(category_id: int, category_service: CategoryService = Depends(get_category_service)):
    return {"message": f"Delete category with id: {category_id}"}