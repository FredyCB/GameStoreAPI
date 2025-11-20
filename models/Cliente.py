from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.sql import func
from utils.database import Base

class Clientes(Base):
    __tablename__ = "Clientes"
    __table_args__ = {"implicit_returning": False}

    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String(200), nullable=False)
    email = Column(String(200))
    telefono = Column(String(50))
    fecha_registro = Column(DateTime, server_default=func.now())
