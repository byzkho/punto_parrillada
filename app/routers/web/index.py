
from fastapi import APIRouter, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

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
    return templates.TemplateResponse("billings/billings.html", {"request": request})

@router.get("/crear-factura")
async def create_bill(request: Request):
    return templates.TemplateResponse("billings/create_bill.html", {"request": request})

@router.get("/ordenes")
async def orders(request: Request):
    return templates.TemplateResponse("orders/orders.html", {"request": request})

@router.get("/crear-orden")
async def create_order(request: Request):
    return templates.TemplateResponse("orders/create_order.html", {"request": request})

@router.get("/usuarios")
async def users(request: Request):
    return templates.TemplateResponse("users/users.html", {"request": request})

@router.get("/crear-usuario")
async def create_user(request: Request):
    return templates.TemplateResponse("users/create_user.html", {"request": request})

@router.get("/mesas")
async def tables(request: Request):
    return templates.TemplateResponse("tables/tables.html", {"request": request})