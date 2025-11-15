from pydantic import BaseModel
from typing import Optional
from datetime import datetime


# Campos que el cliente puede enviar
class ClienteBase(BaseModel):
    nombre: str
    email: Optional[str] = None
    telefono: Optional[str] = None


class ClienteCreate(ClienteBase):
    pass


class ClienteUpdate(ClienteBase):
    pass


class ClienteResponse(ClienteBase):
    id: int
    fecha_registro: Optional[datetime] = None

    class Config:
        orm_mode = True
