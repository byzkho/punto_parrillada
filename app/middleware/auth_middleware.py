
from fastapi import HTTPException
from fastapi.responses import JSONResponse
from starlette.middleware.base import BaseHTTPMiddleware

from application.services.token_service import TokenService
from domain.exceptions.exceptions import InvalidTokenException


class AuthMiddleware(BaseHTTPMiddleware):
    def __init__(self , app, token_service: TokenService):
        super().__init__(app)
        self.token_service = token_service
    
    async def dispatch(self, request, call_next):
        try:
            exempt_routes = ["/auth/login", "/auth/refresh-token", "/api/menu"]
            if any(request.url.path.startswith(route) for route in exempt_routes):
                return await call_next(request)
            token = request.headers.get("Authorization")
            if not token or not token.startswith("Bearer "):
                raise HTTPException(status_code=401, detail="Token no proporcionado")
            token = token.split(" ")[1]
            user = self.token_service.verify_token(token)
            request.state.user = user
            response = await call_next(request)
            return response
        except HTTPException as e:
            return JSONResponse(status_code=e.status_code, content={"detail": e.detail})
        except InvalidTokenException as e:
            return JSONResponse(status_code=401, content={"detail": "Token inválido"})