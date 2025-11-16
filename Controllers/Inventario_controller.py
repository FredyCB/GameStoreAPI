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
        """
        PUT: reemplaza TODO el recurso. Se espera que el cliente envíe
        todas las propiedades necesarias (nombre, precio, stock, ubicacion).
        Usamos query.update() para aplicar los cambios de forma atómica.
        """
        q = db.query(Inventario).filter(Inventario.id == inv_id)
        obj = q.first()
        if not obj:
            return None

        # Construimos el diccionario con los valores a actualizar.
        update_values = {
            "nombre": data.nombre,
            "precio": data.precio,
            "stock": data.stock,
            "ubicacion": data.ubicacion
        }

        try:
            # update() aplica los cambios en la base y es más fiable para
            # este caso "reemplazar todo".
            q.update(update_values, synchronize_session="fetch")
            db.commit()
            # obtener el objeto actualizado y retornarlo
            updated = q.first()
            return updated
        except SQLAlchemyError as e:
            # Si hay error en la BD devolvemos None o lanzamos;
            # aquí se re-lanza para que la ruta lo convierta en 500 con detalle.
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
