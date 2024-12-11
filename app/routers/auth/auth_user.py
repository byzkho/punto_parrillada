
from fastapi import APIRouter, Depends, HTTPException, Request, Response
from application.dto.create_user_dto import CreateUserDTO
from application.dto.login_dto import LoginDto
from application.dto.refresh_token_dto import RefreshTokenDto
from application.services.auth_service import AuthService
from application.services.token_service import TokenService
from application.services.user_service import UserService
from domain.exceptions.exceptions import InvalidCredentialsException
from infrastructure.providers.provider_module import get_auth_service, get_token_service, get_user_service
from app.manager.cookie_manager import CookieManager


router = APIRouter()

@router.post("/login")
def login(credentials: LoginDto, auth_service: AuthService = Depends(get_auth_service)):
    try:
        user = auth_service.login_user(credentials.username, credentials.password)
        return user
    except InvalidCredentialsException as e:
        raise HTTPException(status_code=401, detail=e.detail)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    
@router.post("/refresh-token")
async def refresh_token(data: RefreshTokenDto, request: Request, token_service: TokenService = Depends(get_token_service), user_service: UserService = Depends(get_user_service)):
    body = await request.json()
    payload = token_service.verify_token(data.refresh_token)
    if payload is None:
        raise HTTPException(status_code=401, detail="Invalid refresh token")
    
    db_token = token_service.is_token_in_db(data.refresh_token)
    if not db_token:
        raise HTTPException(status_code=401, detail="Invalid refresh token")

    user = user_service.get_user(payload["id"])
    
    access_token = token_service.create_access_token(user)
    return {"access_token": access_token}
    
@router.post("/logout")
def logout(response: Response, cookie_manager: CookieManager = Depends()):
    cookie_manager.delete_access_token_cookie(response)
    cookie_manager.delete_refresh_token_cookie(response)
    return {"message": "Sesión cerrada correctamente"}

@router.post("/register")
def register_user(create_user_dto: CreateUserDTO, auth_service: AuthService = Depends(get_auth_service)):
    try:
        auth_service.register_user(create_user_dto)
        return {"message": "Usuario registrado correctamente"}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
    
@router.get("/user")
def get_user(
    request: Request,
    token_service: TokenService = Depends(get_token_service),
    auth_service: AuthService = Depends(get_auth_service)
):
    access_token = request.headers.get("Authorization")
    if not access_token:
        raise HTTPException(status_code=401, detail="No se encontró un access token")
    try:
        token = access_token.split("Bearer ")[1]
        user_data = token_service.verify_token(token)
        user = auth_service.find_by_id(user_data["id"])
        if not user:
            raise HTTPException(status_code=401, detail="Usuario no encontrado")
        
        return user
    except InvalidCredentialsException:
        raise HTTPException(status_code=401, detail="Access token no es válido")
    except Exception as e:
        raise HTTPException(status_code=500, detail="Internal server error")