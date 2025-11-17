# Controllers/Inventario_controller.py
from sqlalchemy.orm import Session
from sqlalchemy.exc import SQLAlchemyError
from models.Inventario import Inventario
from models.Juego import Juego
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
        # Previene duplicados por nombre
        existing = db.query(Inventario).filter(Inventario.nombre == data.nombre).first()
        if existing:
            raise ValueError("Ya existe una entrada de inventario con ese nombre")

        obj = Inventario(
            nombre=data.nombre,
            precio=data.precio,
            stock=data.stock,
            ubicacion=data.ubicacion
        )
        try:
            db.add(obj)
            db.commit()
            db.refresh(obj)
        except SQLAlchemyError as e:
            db.rollback()
            raise e

        # Crear o sincronizar el registro en Juegos (si no existe)
        juego = db.query(Juego).filter(Juego.inventario_id == obj.id).first()
        if not juego:
            # NO permitimos duplicados por inventario_id en Juegos; inventario_id es único en Juegos
            j = Juego(
                inventario_id=obj.id,
                nombre=obj.nombre,
                precio=obj.precio,
                descripcion=None
            )
            try:
                db.add(j)
                db.commit()
            except SQLAlchemyError:
                db.rollback()
                # No bloquear creación de inventario: solo registrar el problema
        else:
            # si ya existía, sincronizamos nombre/precio
            juego.nombre = obj.nombre
            juego.precio = obj.precio
            try:
                db.commit()
            except SQLAlchemyError:
                db.rollback()

        return obj

    @staticmethod
    def update(db: Session, inv_id: int, data: InventarioUpdate):
        obj = db.query(Inventario).filter(Inventario.id == inv_id).first()
        if not obj:
            return None

        # Prevención de duplicado por nombre (si cambia el nombre)
        if data.nombre != obj.nombre:
            exists = db.query(Inventario).filter(Inventario.nombre == data.nombre).first()
            if exists:
                raise ValueError("Ya existe una entrada de inventario con ese nombre")

        obj.nombre = data.nombre
        obj.precio = data.precio
        obj.stock = data.stock
        obj.ubicacion = data.ubicacion

        try:
            db.commit()
            db.refresh(obj)
        except SQLAlchemyError as e:
            db.rollback()
            raise e

        # sincronizar en Juegos
        juego = db.query(Juego).filter(Juego.inventario_id == obj.id).first()
        if juego:
            juego.nombre = obj.nombre
            juego.precio = obj.precio
            try:
                db.commit()
            except SQLAlchemyError:
                db.rollback()

        return obj

    @staticmethod
    def delete(db: Session, inv_id: int):
        obj = db.query(Inventario).filter(Inventario.id == inv_id).first()
        if not obj:
            return None

        # Eliminar juego relacionado si existe
        juego = db.query(Juego).filter(Juego.inventario_id == obj.id).first()
        if juego:
            try:
                db.delete(juego)
                db.commit()
            except SQLAlchemyError:
                db.rollback()

        try:
            db.delete(obj)
            db.commit()
        except SQLAlchemyError as e:
            db.rollback()
            raise e

        return obj
