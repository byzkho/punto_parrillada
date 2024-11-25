
from datetime import datetime, timedelta, timezone
from urllib import request
from fastapi import APIRouter, Depends, HTTPException, Response
from fastapi import security
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer
from application.dto.login_dto import LoginDto
from application.services.auth_service import AuthService
from application.services.token_service import TokenService
from domain.exceptions.exceptions import InvalidCredentialsException
from infrastructure.providers.provider_module import get_auth_service, get_token_service


router = APIRouter()

security = HTTPBearer()

@router.post("/login")
def login(
    credentials: LoginDto, 
    response: Response,
    auth_service: AuthService = Depends(get_auth_service), 
    token_service: TokenService = Depends(get_token_service),
):
    try:
        user = auth_service.login_user(credentials.username, credentials.password)
        refresh_token = token_service.create_refresh_token({"username": user.username, "id": user.id})
        access_token = token_service.create_access_token(user)
        expires = datetime.now(timezone.utc) + timedelta(days=2)
        token_service.save_token({
            "token": refresh_token,
            "user_id": user.id
        })
        response.set_cookie(
        "access_token",
        access_token,
        expires=expires,
        httponly=True,
        samesite="Strict",
        )
        return {"access_token": access_token, "refresh_token": refresh_token}
    except InvalidCredentialsException as e:
        raise HTTPException(status_code=401, detail=e.detail)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    
@router.post("/refresh")
def refresh_token(
    response: Response,
    token_service: TokenService = Depends(get_token_service),
):
    try:
        refresh_token = request.cookies.get("refresh_token")
        if not refresh_token:
            raise HTTPException(status_code=401, detail="No se encontró un refresh token")
        
        user_data = token_service.verify_refresh_token(refresh_token)
        access_token = token_service.create_access_token(user_data)

        expires = datetime.now(timezone.utc) + timedelta(days=2)
        response.set_cookie(
            "access_token",
            access_token,
            expires=expires,
            httponly=True,
            samesite="Strict",
        )
        return {"message": "Token renovado correctamente"}
    except Exception:
        raise HTTPException(status_code=401, detail="El refresh token no es válido")
    
@router.post("/logout")
def logout(response: Response):
    response.delete_cookie("access_token")
    return {"message": "Sesión cerrada correctamente"}
    
@router.get("/user")
def get_user(
    credentials: HTTPAuthorizationCredentials = Depends(security), 
    auth_service: AuthService = Depends(get_auth_service),
):
    try:
        token = credentials.credentials
        user = auth_service.find_by_token(token)
        return {"id": user.id, "username": user.username}
    except InvalidCredentialsException as e:
        raise HTTPException(status_code=401, detail=e.detail)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))