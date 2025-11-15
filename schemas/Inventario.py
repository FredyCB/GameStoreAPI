from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class InventarioBase(BaseModel):
    nombre: str
    precio: float
    stock: Optional[int] = None
    ubicacion: Optional[str] = None


class InventarioCreate(InventarioBase):
    pass


class InventarioUpdateStock(BaseModel):
    stock: int


class InventarioUpdatePrecio(BaseModel):
    precio: float


class InventarioResponse(BaseModel):
    id: int
    nombre: str
    precio: float
    stock: int
    fecha_actualizacion: Optional[datetime]

    class Config:
        orm_mode = True
