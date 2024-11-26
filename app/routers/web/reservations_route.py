from fastapi import APIRouter, Form
from fastapi.responses import JSONResponse

router = APIRouter()

@router.post("/reservations")
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