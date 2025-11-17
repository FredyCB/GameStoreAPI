# models/Juego.py
from sqlalchemy import Column, Integer, String, Float, ForeignKey
from utils.database import Base

class Juego(Base):
    __tablename__ = "Juegos"
    __table_args__ = {"implicit_returning": False}

    id = Column(Integer, primary_key=True, index=True)
    inventario_id = Column(Integer, nullable=False, unique=True)  # una entrada de inventario -> 1 registro en juegos
    nombre = Column(String(200), nullable=False)
    precio = Column(Float, nullable=False, default=0.0)
    descripcion = Column(String(1000), nullable=True)
