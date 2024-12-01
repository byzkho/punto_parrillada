# import app
from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from application.services.auth_service import AuthService
from infrastructure.providers.provider_module import injector
from app.middleware.auth_middleware import AuthMiddleware
from application.services.role_service import RoleService
from application.services.token_service import TokenService
from app.manager.cookie_manager import CookieManager
from app.routers.apis import reservations, billing, orders, roles, tables, users,category, menu, dishes
from app.routers.web import index
from app.routers.auth import auth_user
from fastapi.middleware.cors import CORSMiddleware
import os

app = FastAPI()
app.mount("/static", StaticFiles(directory="app/static"), name="static")
app.mount("/reservations/static", StaticFiles(directory="app/templates/reservations/static"), name="reservation_static")
app.mount("/orders/static", StaticFiles(directory="app/templates/orders/static"), name="orders_static")
app.mount("/billings/static", StaticFiles(directory="app/templates/billings/static"), name="billing_static")

role_service = injector.get(RoleService)
token_service = injector.get(TokenService)
cookie_manager = injector.get(CookieManager)
auth_service = injector.get(AuthService)

app.add_middleware(AuthMiddleware, token_service=token_service)

app.add_middleware(CORSMiddleware,
                    allow_origins=[os.environ.get('FRONTEND_URL')],
                    allow_credentials=True,
                    allow_methods=["*"],
                    allow_headers=["*"])

templates = Jinja2Templates(directory="app/templates")
templates.env.globals["current_path"] = lambda request: request.url.path
templates.env.globals["user"] = lambda request: getattr(request.state, "user", None)

app.include_router(index.router)
app.include_router(billing.router, prefix="/api")
app.include_router(orders.router, prefix="/api")
app.include_router(auth_user.router, prefix="/auth")
app.include_router(roles.router, prefix="/roles")
app.include_router(tables.router, prefix="/api")
app.include_router(reservations.router, prefix="/api")
app.include_router(users.router, prefix="/api")
app.include_router(category.router, prefix="/api")
app.include_router(menu.router, prefix="/api")
app.include_router(dishes.router, prefix="/api")
