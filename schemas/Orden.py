from pydantic import BaseModel
from typing import List, Optional
from decimal import Decimal

class DetalleCreate(BaseModel):
    inventario_id: int
    cantidad: int
    precio_unitario: Optional[Decimal] = None

class OrdenCreate(BaseModel):
    cliente_id: int
    detalles: List[DetalleCreate]
    total: Optional[Decimal] = Decimal(0)

class OrdenResponse(BaseModel):
    id: int
    cliente_id: int
    fecha_orden: Optional[str] = None
    total: Optional[Decimal] = None
    estado: Optional[str] = None
    class Config:
        orm_mode = True
