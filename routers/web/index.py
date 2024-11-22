
from fastapi import APIRouter, Depends, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

from routers.auth.verify_role import get_user_with_role

router = APIRouter()

templates = Jinja2Templates(directory="app/templates")

templates.env.globals["current_path"] = lambda request: request.url.path

@router.get("/", response_class=HTMLResponse)
async def read_root(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@router.get("/reservations")
async def get_reservations_form(request: Request, user=Depends(get_user_with_role("admin"))):
    return templates.TemplateResponse("reservations.html", {"request": request})

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