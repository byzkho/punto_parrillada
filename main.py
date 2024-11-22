# import app
from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from routers import reservations
from routers.web import index

app = FastAPI()
app.mount("/static", StaticFiles(directory="app/static"), name="static")

templates = Jinja2Templates(directory="app/templates")

templates.env.globals["current_path"] = lambda request: request.url.path

app.include_router(reservations.router)
app.include_router(index.router)
