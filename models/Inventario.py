from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.sql import func
from sqlalchemy.orm import relationship
from utils.database import Base

class Inventario(Base):
    __tablename__ = "Inventario"
    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String(200), nullable=False)
    ubicacion = Column(String(200))
    fecha_actualizacion = Column(DateTime, server_default=func.now())
    juegos = relationship("Juego", back_populates="inventario", cascade="all, delete-orphan")
