# import app
from fastapi import FastAPI, Request
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from app.middleware.token_refresh_middleware import TokenRefreshMiddleware
from application.services.auth_service import AuthService
from infrastructure.providers.provider_module import injector
from app.middleware.auth_middleware import AuthMiddleware
from application.services.role_service import RoleService
from application.services.token_service import TokenService
from app.manager.cookie_manager import CookieManager
from app.routers.apis import reservations, billing, orders, roles, tables
from app.routers.web import index
from app.routers.auth import auth_user

app = FastAPI()
app.mount("/static", StaticFiles(directory="app/static"), name="static")
app.mount("/reservations/static", StaticFiles(directory="app/templates/reservations/static"), name="reservation_static")


role_service = injector.get(RoleService)
token_service = injector.get(TokenService)
cookie_manager = injector.get(CookieManager)
auth_service = injector.get(AuthService)

app.add_middleware(AuthMiddleware, auth_service=auth_service, token_service=token_service)
app.add_middleware(TokenRefreshMiddleware, token_service=token_service, cookie_manager=cookie_manager)

templates = Jinja2Templates(directory="app/templates")
templates.env.globals["current_path"] = lambda request: request.url.path
templates.env.globals["user"] = lambda request: getattr(request.state, "user", None)

app.include_router(billing.router)
app.include_router(orders.router)
app.include_router(index.router)
app.include_router(auth_user.router, prefix="/auth")
app.include_router(roles.router, prefix="/roles")
app.include_router(tables.router, prefix="/tables")
app.include_router(reservations.router, prefix="/api")