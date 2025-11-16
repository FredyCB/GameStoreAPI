from pydantic import BaseModel
from typing import Optional

class JuegoCatalogoResponse(BaseModel):
    inventario_id: int
    nombre: str
    precio: float

    model_config = {
        "from_attributes": True
    }

class JuegoSearchResponse(BaseModel):
    inventario_id: int
    nombre: str
    precio: float

    model_config = {
        "from_attributes": True
    }
