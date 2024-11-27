
from datetime import datetime, timedelta, timezone
from urllib import request
from fastapi import APIRouter, Depends, HTTPException, Request, Response
from fastapi import security
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer
from app.schemas.login_schema import LoginSchema
from app.schemas.user_schema import UserSchema
from application.dto.create_user_dto import CreateUserDTO
from application.dto.login_dto import LoginDto
from application.services.auth_service import AuthService
from application.services.token_service import TokenService
from domain.exceptions.exceptions import InvalidCredentialsException
from infrastructure.providers.provider_module import get_auth_service, get_token_service
from app.manager.cookie_manager import CookieManager


router = APIRouter()

security = HTTPBearer()

@router.post("/login", response_model=LoginSchema)
async def login(
    request: Request,
    credentials: LoginDto, 
    response: Response, 
    auth_service: AuthService = Depends(get_auth_service),
    cookie_manager: CookieManager = Depends()
):
    result = auth_service.login_user(credentials.username, credentials.password)
    cookie_manager.set_access_token_cookie(response, result["access_token"], result["expires"])
    cookie_manager.set_refresh_token_cookie(response, result["refresh_token"], result["expires"])
    return {"access_token": result["access_token"], "refresh_token": result["refresh_token"], "user": result["user"]}
    
@router.post("/refresh")
def refresh_token(
    response: Response,
    token_service: TokenService = Depends(get_token_service),
    cookie_manager: CookieManager = Depends()
):
    try:
        refresh_token = request.cookies.get("refresh_token")
        if not refresh_token:
            raise HTTPException(status_code=401, detail="No se encontró un refresh token")
        
        user_data = token_service.verify_token(refresh_token)
        access_token = token_service.create_access_token(user_data)

        expires = datetime.now(timezone.utc) + timedelta(minutes=15)
        cookie_manager.set_access_token_cookie(response, access_token, expires)
        return {"message": "Token renovado correctamente"}
    except Exception:
        raise HTTPException(status_code=401, detail="El refresh token no es válido")
    
@router.post("/logout")
def logout(response: Response, cookie_manager: CookieManager = Depends()):
    cookie_manager.delete_access_token_cookie(response)
    cookie_manager.delete_refresh_token_cookie(response)
    return {"message": "Sesión cerrada correctamente"}

@router.post("/register")
def register_user(create_user_dto: CreateUserDTO, auth_service: AuthService = Depends(get_auth_service)):
    try:
        print(f"Valor en ruta antes del servicio: {create_user_dto.role} ({type(create_user_dto.role)})")
        auth_service.register_user(create_user_dto)
        return {"message": "Usuario registrado correctamente"}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
    
@router.get("/user", response_model=UserSchema)
def get_user(
    request: Request,
    token_service: TokenService = Depends(get_token_service),
    auth_service: AuthService = Depends(get_auth_service)
):
    access_token = request.cookies.get("access_token")
    if not access_token:
        raise HTTPException(status_code=401, detail="No se encontró un access token")
    
    try:
        user_data = token_service.verify_token(access_token)
        user = auth_service.find_by_id(user_data["id"])
        if not user:
            raise HTTPException(status_code=401, detail="Usuario no encontrado")
        
        return user
    except InvalidCredentialsException:
        raise HTTPException(status_code=401, detail="Access token no es válido")