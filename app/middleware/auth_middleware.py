from fastapi import Request, HTTPException
from fastapi.responses import JSONResponse
from starlette.middleware.base import BaseHTTPMiddleware
from application.services.token_service import TokenService

class AuthMiddleware(BaseHTTPMiddleware):        
    async def dispatch(self, request: Request, call_next):
        public_routes = ["/", "/orders", "/auth/login", "/auth/register", "/auth/refresh"]
        if any(request.url.path.startswith(route) for route in public_routes):
            return await call_next(request)
        try:
            request.state.user = None

            token = request.cookies.get("access_token")
            if token:
                credentials_exception = HTTPException(
                    status_code=401,
                    detail="Credenciales no válidas",
                    headers={"WWW-Authenticate": "Bearer"},
                )
                try:
                    user = TokenService.verify_token(token, credentials_exception)
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