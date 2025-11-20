from pydantic import BaseModel
from decimal import Decimal
from typing import Optional

class DetalleItem(BaseModel):
    nombre_juego: str
    cantidad: int

class DetalleOrdenBase(BaseModel):
    inventario_id: int
    nombre_inventario: str
    cantidad: int
    precio_unitario: Decimal

    model_config = {
        "from_attributes": True
    }

class DetalleOrdenResponse(DetalleOrdenBase):
    id: int
