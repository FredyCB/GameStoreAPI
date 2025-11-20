from pydantic import BaseModel
from datetime import datetime
from typing import List
from .Detalle_Orden import DetalleOrdenResponse, DetalleItem

class OrdenCreate(BaseModel):
    cliente_id: int
    juegos: List[DetalleItem]

class OrdenResponse(BaseModel):
    id: int
    cliente_id: int
    cliente_nombre: str
    fecha_orden: datetime
    total: float
    estado: str
    detalles: List[DetalleOrdenResponse] = []

    model_config = {
        "from_attributes": True
    }
