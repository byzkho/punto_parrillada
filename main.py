# import app
from fastapi import FastAPI, Request
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from infrastructure.providers.provider_module import injector
from app.middleware.auth_middleware import AuthMiddleware
from application.services.role_service import RoleService
from routers.apis import reservations, billing, orders, roles, tables
from routers.web import index
from routers.auth import auth_user

app = FastAPI()
app.mount("/static", StaticFiles(directory="app/static"), name="static")
app.mount("/reservations/static", StaticFiles(directory="app/templates/reservations/static"), name="reservation_static")


role_service = injector.get(RoleService)

app.add_middleware(AuthMiddleware)

templates = Jinja2Templates(directory="app/templates")

templates.env.globals["current_path"] = lambda request: request.url.path
templates.env.globals["user"] = lambda request: getattr(request.state, "user", None)

app.include_router(reservations.router)
app.include_router(billing.router)
app.include_router(orders.router)
app.include_router(index.router)
app.include_router(auth_user.router, prefix="/auth")
app.include_router(roles.router, prefix="/roles")
app.include_router(tables.router, prefix="/tables")