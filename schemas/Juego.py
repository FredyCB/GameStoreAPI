from pydantic import BaseModel
from typing import Optional

class JuegoBase(BaseModel):
    nombre_juego: str
    inventario_id: int

class JuegoCreate(JuegoBase):
    pass

class JuegoUpdate(BaseModel):
    nombre_juego: Optional[str] = None
    inventario_id: Optional[int] = None

class JuegoResponse(JuegoBase):
    id: int

    class Config:
        orm_mode = True
