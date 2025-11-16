# models/Juegos.py
from sqlalchemy import Column, Float, Integer, String, ForeignKey
from utils.database import Base

class Juego(Base):
    __tablename__ = "Juegos"
    id = Column(Integer, primary_key=True, index=True)
    inventario_id = Column(Integer, ForeignKey("Inventario.id"), nullable=False, unique=True)
    nombre = Column(String(250), nullable=False)
    precio = Column(Float, nullable=False)
