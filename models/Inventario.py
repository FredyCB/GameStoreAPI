from sqlalchemy import Column, Integer, String, Float, DateTime
from sqlalchemy.sql import func
from utils.database import Base

class Inventario(Base):
    __tablename__ = "Inventario"

    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String(200), nullable=False)
    precio = Column(Float, nullable=False)
    ubicacion = Column(String(200))
    stock = Column(Integer, default=0)
    fecha_actualizacion = Column(DateTime, server_default=func.now(), onupdate=func.now())
