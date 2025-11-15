from pydantic import BaseModel
from typing import Optional

class InventarioBase(BaseModel):
    nombre: str
    ubicacion: Optional[str] = None

class InventarioCreate(InventarioBase): ...
class InventarioUpdate(InventarioBase): ...

class InventarioResponse(InventarioBase):
    id: int
    fecha_actualizacion: Optional[str] = None
    class Config:
        orm_mode = True
