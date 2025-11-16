from sqlalchemy.orm import Session
from sqlalchemy.exc import SQLAlchemyError
from models.Inventario import Inventario
from schemas.Inventario import InventarioCreate, InventarioUpdate


class InventarioController:

    @staticmethod
    def list_all(db: Session):
        return db.query(Inventario).all()

    @staticmethod
    def get(db: Session, inv_id: int):
        return db.query(Inventario).filter(Inventario.id == inv_id).first()

    @staticmethod
    def create(db: Session, data: InventarioCreate):
        # 🔎 Validar nombre duplicado
        exists = db.query(Inventario).filter(
            Inventario.nombre == data.nombre
        ).first()

        if exists:
            raise ValueError("Ya existe un juego con ese nombre en el inventario.")

        obj = Inventario(
            nombre=data.nombre,
            precio=data.precio,
            stock=data.stock,
            ubicacion=data.ubicacion
        )
        db.add(obj)
        db.commit()
        db.refresh(obj)
        return obj

    @staticmethod
    def update(db: Session, inv_id: int, data: InventarioUpdate):
        q = db.query(Inventario).filter(Inventario.id == inv_id)
        obj = q.first()
        if not obj:
            return None

        # 🛑 Evitar duplicado con otro registro
        name_conflict = db.query(Inventario).filter(
            Inventario.nombre == data.nombre,
            Inventario.id != inv_id
        ).first()

        if name_conflict:
            raise ValueError("Otro inventario ya usa ese nombre.")

        update_values = {
            "nombre": data.nombre,
            "precio": data.precio,
            "stock": data.stock,
            "ubicacion": data.ubicacion
        }

        try:
            q.update(update_values, synchronize_session="fetch")
            db.commit()
            return q.first()
        except SQLAlchemyError as e:
            db.rollback()
            raise e

    @staticmethod
    def delete(db: Session, inv_id: int):
        obj = db.query(Inventario).filter(Inventario.id == inv_id).first()
        if not obj:
            return None

        db.delete(obj)
        db.commit()
        return obj
