from sqlalchemy import Column, Integer, String, DateTime, Float
from sqlalchemy.sql import func
from utils.database import Base

class Inventario(Base):
    __tablename__ = "Inventario"

    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String(200), nullable=False)
    precio = Column(Float, nullable=False, default=0.0)
    stock = Column(Integer, nullable=False, default=0)
    ubicacion = Column(String(200), nullable=True)

    fecha_actualizacion = Column(
        DateTime,
        server_default=func.now(),
        onupdate=func.now()
    )
