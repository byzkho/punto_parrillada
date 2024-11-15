"""from fastapi import FastAPI, Request
from app.database import Base, engine
from routers import reservations, orders, billing, users
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse

app = FastAPI()
templates = Jinja2Templates(directory="templates")
app.include_router(reservations.router)

@app.get("/")
async def home(request: Request):
    return templates.TemplateResponse("reservations.html", {"request": request})

@app.get("/reservations", response_class=HTMLResponse)
async def read_reservations(request: Request):
    return templates.TemplateResponse("reservations.html", {"request": request})


# Crea todas las tablas en la base de datos
Base.metadata.create_all(bind=engine)

app = FastAPI()

# Incluye los routers de cada módulo
app.include_router(users.router)
app.include_router(reservations.router)
app.include_router(orders.router)
app.include_router(billing.router)

@app.get("/")
def root():
    return {"message": "Bienvenido a Punto Parrillada RD"}"""
# import app
from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates

from routers import reservations  # Asegúrate de que tu import esté bien configurado

# Configurar la carpeta de archivos estáticos

# Monta la carpeta 'static' para servir archivos estáticos
#app.mount("/static", StaticFiles(directory="app/static"), name="static")

app = FastAPI()
templates = Jinja2Templates(directory="app/templates")

# Ruta para el menú principal
@app.get("/menu")
async def menu(request: Request):
    return templates.TemplateResponse("menu.html", {"request": request})

# Ruta para el index
@app.get("/")
async def index(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

# Ruta para facturación
@app.get("/billing")
async def billing(request: Request):
    return templates.TemplateResponse("facturacion.html", {"request": request})

# Ruta para las órdenes
@app.get("/orders")
async def orders(request: Request):
    return templates.TemplateResponse("ordenes.html", {"request": request})

# Ruta para ventas
@app.get("/sales")
async def sales(request: Request):
    return templates.TemplateResponse("ventas.html", {"request": request})

# Ruta para el registro de usuario
@app.get("/register")
async def register(request: Request):
    return templates.TemplateResponse("registrarse.html", {"request": request})

# Incluye el router de reservaciones, si lo tienes configurado como un router
app.include_router(reservations.router)


