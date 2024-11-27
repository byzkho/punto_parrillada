# FILE: auth_middleware.py
from fastapi import Request, HTTPException
from fastapi.responses import JSONResponse, RedirectResponse
from starlette.middleware.base import BaseHTTPMiddleware
from application.services.auth_service import AuthService
from application.services.token_service import TokenService
from domain.exceptions.exceptions import InvalidCredentialsException

class AuthMiddleware(BaseHTTPMiddleware):
    def __init__(self, app, auth_service: AuthService, token_service: TokenService, excluded_paths: list[str] = None):
        super().__init__(app)
        self.auth_service = auth_service
        self.token_service = token_service
        self.excluded_paths = excluded_paths or []
    
    async def dispatch(self, request: Request, call_next):
        path = request.url.path
        if any(path.startswith(excluded_path) for excluded_path in self.excluded_paths):
            return await call_next(request)
        
        try:
            request.state.user = None
            token = request.cookies.get("access_token")
            if token:
                try:
                    payload = self.token_service.verify_token(token)
                    user = self.auth_service.find_by_id(payload.get("id"))
                    if user:
                        request.state.user = user
                except InvalidCredentialsException as e:
                    if "expired" in str(e).lower():
                        request.cookies.pop("access_token")
                        return request
                    raise HTTPException(status_code=401, detail=str(e))

            # Si la ruta es "/", no devolver un error 401
            if path == "/" and not request.state.user:
                return await call_next(request)

            if not request.state.user:
                return RedirectResponse(url="/", status_code=307)

            return await call_next(request)

        except HTTPException as e:
            return JSONResponse(status_code=e.status_code, content={"detail": e.detail})
        except Exception as e:
            return JSONResponse(status_code=500, content={"detail": str(e)})