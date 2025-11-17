# Controllers/Juego_controller.py
from sqlalchemy.orm import Session
from sqlalchemy.exc import SQLAlchemyError
from models.Juego import Juego
from schemas.Juego import JuegoCreate, JuegoUpdate


class JuegoController:

    @staticmethod
    def list_all(db: Session):
        return db.query(Juego).all()

    @staticmethod
    def get_by_id(db: Session, juego_id: int):
        return db.query(Juego).filter(Juego.id == juego_id).first()

    @staticmethod
    def get_by_inventario_id(db: Session, inventario_id: int):
        return db.query(Juego).filter(Juego.inventario_id == inventario_id).first()

    @staticmethod
    def find_by_nombre(db: Session, nombre: str):
        return db.query(Juego).filter(Juego.nombre.ilike(f"%{nombre}%")).all()

    @staticmethod
    def create(db: Session, data: JuegoCreate):

        exists_inv = db.query(Juego).filter(
            Juego.inventario_id == data.inventario_id
        ).first()
        if exists_inv:
            raise ValueError("Ya existe un juego para ese inventario_id")

        exists_name = db.query(Juego).filter(
            Juego.nombre == data.nombre
        ).first()
        if exists_name:
            raise ValueError("Ya existe un juego con ese nombre en catálogo")

        obj = Juego(
            inventario_id=data.inventario_id,
            nombre=data.nombre,
            precio=data.precio,
            descripcion=data.descripcion
        )

        try:
            db.add(obj)
            db.commit()
            db.refresh(obj)
        except SQLAlchemyError as e:
            db.rollback()
            raise e

        return obj

    @staticmethod
    def update(db: Session, juego_id: int, data: JuegoUpdate):
        obj = db.query(Juego).filter(Juego.id == juego_id).first()
        if not obj:
            return None

        if data.inventario_id != obj.inventario_id:
            exists = db.query(Juego).filter(
                Juego.inventario_id == data.inventario_id
            ).first()
            if exists:
                raise ValueError("Ya existe un juego para ese inventario_id")

        if data.nombre != obj.nombre:
            existsn = db.query(Juego).filter(
                Juego.nombre == data.nombre
            ).first()
            if existsn:
                raise ValueError("Ya existe un juego con ese nombre en catálogo")

        obj.inventario_id = data.inventario_id
        obj.nombre = data.nombre
        obj.precio = data.precio
        obj.descripcion = data.descripcion

        try:
            db.commit()
            db.refresh(obj)
        except SQLAlchemyError as e:
            db.rollback()
            raise e

        return obj

    @staticmethod
    def delete(db: Session, juego_id: int):
        obj = db.query(Juego).filter(Juego.id == juego_id).first()
        if not obj:
            return None

        try:
            db.delete(obj)
            db.commit()
        except SQLAlchemyError as e:
            db.rollback()
            raise e

        return obj
