from fastapi import APIRouter, Depends

from app.schemas.menu_schema import MenuSchema
from application.dto.menu_dto import MenuDTO
from application.services.menu_service import MenuService
from infrastructure.providers.provider_module import get_menu_service


router = APIRouter()

@router.get("/menus/")
async def get_all_menus(menu_service: MenuService = Depends(get_menu_service)):
    return menu_service.get_menu()

@router.get("/menus/{menu_id}")
async def get_menu(menu_id: int, menu_service: MenuService = Depends(get_menu_service)):
    try:
        return menu_service.get_menu_by_id(menu_id)
    except Exception as e:
        return {"message": str(e.detail["msg"])}

@router.post("/menus")
async def create_menu(menu_dto: MenuDTO, menu_service: MenuService = Depends(get_menu_service)):
    menu_service.create_menu(menu_dto)
    return {"message": "Menu created successfully"}

@router.patch("/menus/{menu_id}")
async def update_menu(menu_id: int, menu_dto: MenuDTO, menu_service: MenuService = Depends(get_menu_service)):
    return menu_service.update_menu(menu_dto, menu_id)

@router.delete("/menus/{menu_id}")
async def delete_menu(menu_id: int, menu_service: MenuService = Depends(get_menu_service)):
    return {"message": f"Delete menu with id: {menu_id}"}