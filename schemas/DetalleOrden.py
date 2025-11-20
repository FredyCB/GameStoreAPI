from pydantic import BaseModel
from decimal import Decimal

class DetalleItem(BaseModel):
    nombre_juego: str
    cantidad: int

class DetalleOrdenBase(BaseModel):
    inventario_id: int
    nombre_inventario: str
    cantidad: int
    precio_unitario: Decimal

class DetalleOrdenResponse(DetalleOrdenBase):
    id: int

    model_config = {
        "from_attributes": True
    }
