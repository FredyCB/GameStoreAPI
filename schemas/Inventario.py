from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class InventarioBase(BaseModel):
    nombre: str
    precio: float
    stock: Optional[int] = None
    ubicacion: Optional[str] = None


class InventarioCreate(InventarioBase): ...
class InventarioUpdate(InventarioBase): ...

class InventarioResponse(InventarioBase):
    id: int
    fecha_actualizacion: Optional[datetime] = None

    class Config:
        orm_mode = True
