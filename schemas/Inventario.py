from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class InventarioBase(BaseModel):
    nombre: str
    precio: float
    stock: int
    ubicacion: Optional[str] = None

class InventarioCreate(InventarioBase):
    pass

class InventarioUpdate(InventarioBase):
    pass

class InventarioResponse(InventarioBase):
    id: int
    fecha_actualizacion: Optional[datetime]

    model_config = {
        "from_attributes": True
    }
