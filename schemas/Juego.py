# schemas/Juego.py
from pydantic import BaseModel
from decimal import Decimal

class JuegoBase(BaseModel):
    nombre: str
    precio: Decimal

class JuegoCreate(JuegoBase):
    pass

class JuegoUpdate(JuegoBase):
    pass

class JuegoResponse(JuegoBase):
    id: int
    inventario_id: int

    class Config:
        orm_mode = True
