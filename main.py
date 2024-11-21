# import app
from fastapi import FastAPI, Request, Form
from fastapi.responses import JSONResponse
# from fastapi.responses import RedirectResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from starlette.responses import HTMLResponse

from routers import reservations  # Asegúrate de que tu import esté bien configurado

# Configurar la carpeta de archivos estáticos

# Monta la carpeta 'static' para servir archivos estáticos

app = FastAPI()
app.mount("/static", StaticFiles(directory="app/static"), name="static")

app = FastAPI()
templates = Jinja2Templates(directory="app/templates")

@app.get("/", response_class=HTMLResponse)
async def read_root(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

# Ruta para mostrar el formulario de reservaciones
@app.get("/reservations")
async def get_reservations_form(request: Request):
    return templates.TemplateResponse("reservations.html", {"request": request})

# Ruta para manejar el formulario de reservaciones
@app.post("/reservations")
async def create_reservation(
    cliente: str = Form(...),
    mesa: int = Form(...),
    cantidad: int = Form(...),
    fecha: str = Form(...),
    estado: str = Form(...),
):
    # Simulación de lógica (puedes guardar en una base de datos o procesar datos)
    return JSONResponse(
        content={
            "message": "Reservación creada exitosamente",
            "data": {

                "cliente": cliente,
                "mesa": mesa,
                "cantidad": cantidad,
                "fecha": fecha,
                "estado": estado,
            },
        }
    )

    # Aquí se procesarían los datos de la reservación (guardar en base de datos, etc.)
#print(f"Reservación creada: Cliente={cliente}, Mesa={mesa}, Cantidad={cantidad}, Fecha={fecha}, Estado={estado}")
    #return RedirectResponse(url="/reservations", status_code=303)

# Ruta para crear un nuevo cliente
@app.get("/new-client")
async def new_client(request: Request):
    # Renderiza una página para crear un nuevo cliente
    return templates.TemplateResponse("nuevo_cliente.html", {"request": request})

# Ruta para ver mesas disponibles
@app.get("/view-tables")
async def view_tables(request: Request):
    # Renderiza una página que muestre las mesas disponibles
    return templates.TemplateResponse("ver_mesas.html", {"request": request})

app.mount("/static", StaticFiles(directory="app/static"), name="static")
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
""" @app.get("/sales")
async def sales(request: Request):
    return templates.TemplateResponse("ventas.html", {"request": request})"""

# Ruta para el registro de usuario
""" @app.get("/register")
async def register(request: Request):
    return templates.TemplateResponse("registrarse.html", {"request": request})"""

# Incluye el router de reservaciones, si lo tienes configurado como un router
app.include_router(reservations.router)


