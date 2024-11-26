
from fastapi import APIRouter, Depends, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
import injector

from application.services.role_service import RoleService
from infrastructure.providers.provider_module import get_reservation_service, get_role_service

router = APIRouter()

templates = Jinja2Templates(directory="app/templates")

templates.env.globals["current_path"] = lambda request: request.url.path
templates.env.globals["user"] = lambda request: getattr(request.state, "user", None)

@router.get("/", response_class=HTMLResponse)
async def read_root(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@router.get("/reservaciones")
async def get_reservations_form(request: Request):
    return templates.TemplateResponse("reservations/reservations.html", {"request": request})

@router.get("/mis-reservaciones")
async def get_my_reservations(request: Request):
    return templates.TemplateResponse("reservations/my_reservations.html", {"request": request})

@router.get("/menu")
async def menu(request: Request):
    return templates.TemplateResponse("menu.html", {"request": request})

@router.get("/ver-mesas")
async def view_tables(request: Request):
    return templates.TemplateResponse("ver_mesas.html", {"request": request})

@router.get("/facturaciones")
async def billing(request: Request):
    return templates.TemplateResponse("facturacion.html", {"request": request})

@router.get("/ordenes")
async def orders(request: Request):
    return templates.TemplateResponse("ordenes.html", {"request": request})