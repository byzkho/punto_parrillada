
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

@router.get("/reservations")
async def get_reservations_form(
    request: Request, 
    role_service = Depends(get_role_service),
    reservation_service = Depends(get_reservation_service)):
    reservations = reservation_service.get_by_user(request.state.user["id"])
    return templates.TemplateResponse(
        "reservations/reservations.html", 
        {
            "request": request,
            "roles": role_service.get_all(),
            "reservations": reservations
        }
    )


@router.get("/menu")
async def menu(request: Request):
    return templates.TemplateResponse("menu.html", {"request": request})

@router.get("/new-client")
async def new_client(request: Request):
    return templates.TemplateResponse("nuevo_cliente.html", {"request": request})

@router.get("/view-tables")
async def view_tables(request: Request):
    return templates.TemplateResponse("ver_mesas.html", {"request": request})

@router.get("/billing")
async def billing(request: Request):
    return templates.TemplateResponse("facturacion.html", {"request": request})

@router.get("/orders")
async def orders(request: Request):
    return templates.TemplateResponse("ordenes.html", {"request": request})