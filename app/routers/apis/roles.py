from fastapi import APIRouter, Depends

from infrastructure.providers.provider_module import get_role_service


router = APIRouter()

@router.get("/")
def get_roles(role_service = Depends(get_role_service)):
    return role_service.get_all()