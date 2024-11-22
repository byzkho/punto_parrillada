# import app
from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from app.config.database.init_db import engine
from app.config.database.database import Base
from routers import reservations
from routers.web import index

async def async_startup(app: FastAPI):
    Base.metadata.create_all(bind=engine)
    yield

app = FastAPI(
    lifespan=async_startup
)
app.mount("/static", StaticFiles(directory="app/static"), name="static")

templates = Jinja2Templates(directory="app/templates")

templates.env.globals["current_path"] = lambda request: request.url.path

app.include_router(reservations.router)
app.include_router(index.router)
