from pydantic import BaseModel
from typing import List
from datetime import datetime

class OrdenJuegoItem(BaseModel):
    nombre_juego: str
    cantidad: int

class OrdenCreate(BaseModel):
    cliente_id: int
    juegos: List[OrdenJuegoItem]

class OrdenResponse(BaseModel):
    id: int
    cliente_id: int
    cliente_nombre: str
    fecha_orden: datetime
    total: float
    estado: str

    model_config = {
        "from_attributes": True
    }
