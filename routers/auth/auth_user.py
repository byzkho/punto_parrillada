
from fastapi import APIRouter
import fastapi_users

from app.config.fastapi_users.session_fastapi_users import get_jwt_strategy


router = APIRouter()

router.include_router(
    fastapi_users.get_auth_router(get_jwt_strategy()),
    prefix="/auth/jwt",
    tags=["auth"],
)

# Rutas para registro de usuarios
router.include_router(
    fastapi_users.get_register_router(),
    prefix="/auth",
    tags=["auth"],
)

# Rutas para recuperar información de usuarios
router.include_router(
    fastapi_users.get_users_router(),
    prefix="/users",
    tags=["users"],
)