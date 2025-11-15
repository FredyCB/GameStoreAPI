from pydantic import BaseModel
from typing import Optional
from decimal import Decimal

class JuegoBase(BaseModel):
    inventario_id: int
    titulo: str
    descripcion: Optional[str] = None
    precio: Optional[Decimal] = None

class JuegoCreate(JuegoBase): ...
class JuegoUpdate(JuegoBase): ...

class JuegoResponse(JuegoBase):
    id: int
    class Config:
        orm_mode = True
