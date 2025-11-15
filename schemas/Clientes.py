from pydantic import BaseModel
from typing import Optional

class ClienteBase(BaseModel):
    nombre: str
    email: Optional[str] = None
    telefono: Optional[str] = None

class ClienteCreate(ClienteBase): ...
class ClienteUpdate(ClienteBase): ...

class ClienteResponse(ClienteBase):
    id: int
    fecha_registro: Optional[str] = None
    class Config:
        orm_mode = True
