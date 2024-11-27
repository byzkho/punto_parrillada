# FILE: auth_middleware.py
from fastapi import Request, HTTPException
from fastapi.responses import JSONResponse
from starlette.middleware.base import BaseHTTPMiddleware
from application.services.auth_service import AuthService
from application.services.token_service import TokenService

class AuthMiddleware(BaseHTTPMiddleware):
    def __init__(self, app, auth_service: AuthService, token_service: TokenService):
        super().__init__(app)
        self.auth_service = auth_service
        self.token_service = token_service
    
    async def dispatch(self, request: Request, call_next):
        public_routes = ["/orders", "/auth/register", "/auth/refresh", "/auth/login"]
        if any(request.url.path.startswith(route) for route in public_routes):
            print("solo llega al return")
            return await call_next(request)
        print("pasa por el try")
        try:
            request.state.user = None
            print("request state user es None ahora")
            token = request.cookies.get("access_token")
            if token:
                try:
                    payload = self.token_service.verify_token(token)
                    user = self.auth_service.find_by_id(payload.get("id"))
                    print(user)
                    if user:
                        request.state.user = user
                except Exception as e:
                    raise HTTPException(500, detail=str(e))

            if not request.state.user:
                raise HTTPException(
                    status_code=401,
                    detail="No autenticado. Por favor, inicia sesión."
                )

            return await call_next(request)

        except HTTPException as e:
            return JSONResponse(status_code=e.status_code, content={"detail": e.detail})
        except Exception as e:
            return JSONResponse(status_code=500, content={"detail": str(e)})