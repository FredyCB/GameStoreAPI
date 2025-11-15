from sqlalchemy.orm import Session
from models.Inventario import Inventario
from schemas.Inventario import InventarioCreate

class InventarioController:
    @staticmethod
    def get(db: Session, inv_id: int):
        return db.query(Inventario).filter(Inventario.id == inv_id).first()

    @staticmethod
    def create(db: Session, data: InventarioCreate):
        obj = Inventario()
        setattr(obj, 'nombre', data.nombre)
        setattr(obj, 'ubicacion', data.ubicacion)
        db.add(obj); db.commit(); db.refresh(obj)
        return obj

    @staticmethod
    def update(db: Session, inv_id: int, data: InventarioCreate):
        obj = db.query(Inventario).filter(Inventario.id == inv_id).first()
        if not obj: return None
        setattr(obj, 'nombre', data.nombre)
        setattr(obj, 'ubicacion', data.ubicacion)
        db.commit(); db.refresh(obj)
        return obj
