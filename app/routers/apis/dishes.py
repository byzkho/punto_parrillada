from fastapi import APIRouter, Depends

from application.dto.dish_dto import DishDTO
from application.services.dish_service import DishService
from infrastructure.providers.provider_module import get_dish_service

router = APIRouter()

@router.get("/dishes/")
def get_dishes(dish_service: DishService = Depends(get_dish_service)):
    return dish_service.get_dishes()

@router.get("/dishes/{dish_id}")
def get_dish(dish_id: int, dish_service: DishService = Depends(get_dish_service)):
    try:
        return dish_service.get_dish(dish_id)
    except Exception as e:
        return {"message": str(e.detail["msg"])}

@router.post("/dishes")
def create_dish(dish_dto: DishDTO,dish_service: DishService = Depends(get_dish_service)):
    dish_service.create_dish(dish_dto)
    return {"message": "Dish created successfully"}

@router.get("/dishes/menu/{menu_id}")
def get_by_menu(menu_id: int, dish_service: DishService = Depends(get_dish_service)):
    return dish_service.get_by_menu(menu_id)