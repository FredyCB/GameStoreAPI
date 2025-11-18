# schemas/Juego.py
from pydantic import BaseModel
from typing import Optional


class JuegoBase(BaseModel):
    inventario_id: int
    nombre: str
    precio: float
    descripcion: Optional[str] = None

    model_config = {
        "from_attributes": True
    }


class JuegoCreate(JuegoBase):
    pass


class JuegoUpdate(JuegoBase):
    pass


class JuegoResponse(JuegoBase):
    id: int

