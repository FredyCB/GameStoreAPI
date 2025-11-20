from sqlalchemy.orm import Session
from sqlalchemy.exc import SQLAlchemyError
from typing import List

from models.Cliente import Clientes
from models.Inventario import Inventario
from models.Orden import Orden
from models.Detalle_Orden import DetalleOrden

# Importa schemas solo si los necesitas dentro del controlador (no obligatorio)
# from schemas.Orden import OrdenCreate

class OrdenController:

    @staticmethod
    def list_all(db: Session) -> List[Orden]:
        # devuelve todas las ordenes (con sus relaciones si las quieres serializar)
        return db.query(Orden).all()

    @staticmethod
    def get(db: Session, orden_id: int):
        # trae la orden con sus detalles (por la relación definida en el modelo)
        return db.query(Orden).filter(Orden.id == orden_id).first()

    @staticmethod
    def create(db: Session, data):
        """
        data es OrdenCreate: { cliente_id: int, juegos: [{nombre_juego, cantidad}, ...] }

        - valida cliente
        - crea cabecera de orden con cliente_id y cliente_nombre
        - crea los DetalleOrden buscando inventario por nombre_juego
        - calcula total automático
        - retorna la orden con detalles
        """
        # 1) validar cliente
        cliente = db.query(Clientes).filter(Clientes.id == data.cliente_id).first()
        if not cliente:
            raise ValueError("Cliente no encontrado")

        # 2) crear la orden (encabezado)
        orden = Orden(
            cliente_id=cliente.id,
            cliente_nombre=cliente.nombre,
            estado="Pendiente",
            total=0
        )

        try:
            db.add(orden)
            db.commit()
            db.refresh(orden)
        except SQLAlchemyError as e:
            db.rollback()
            raise e

        total = 0

        # 3) recorrer juegos y crear detalles
        for item in data.juegos:
            inv = db.query(Inventario).filter(Inventario.nombre == item.nombre_juego).first()
            if not inv:
                # si alguno de los juegos no existe, revertimos toda la creación
                # y devolvemos error para que la ruta retorne 400
                db.delete(orden)
                db.commit()
                raise ValueError(f"Juego '{item.nombre_juego}' no existe en inventario")

            detalle = DetalleOrden(
                orden_id=orden.id,
                inventario_id=inv.id,
                nombre_inventario=inv.nombre,
                cantidad=item.cantidad,
                precio_unitario=inv.precio
            )

            subtotal = float(inv.precio) * int(item.cantidad)
            total += subtotal

            try:
                db.add(detalle)
                db.commit()
            except SQLAlchemyError as e:
                db.rollback()
                # intentar eliminar orden por consistencia
                try:
                    db.delete(orden)
                    db.commit()
                except:
                    db.rollback()
                raise e

        # 4) actualizar total en la orden
        try:
            orden.total = total
            db.commit()
            db.refresh(orden)
        except SQLAlchemyError as e:
            db.rollback()
            raise e

        # 5) traer la orden actualizada con sus detalles y retornarla
        orden = db.query(Orden).filter(Orden.id == orden.id).first()
        return orden

    @staticmethod
    def delete(db: Session, orden_id: int):
        orden = db.query(Orden).filter(Orden.id == orden_id).first()
        if not orden:
            return None

        try:
            db.delete(orden)
            db.commit()
        except SQLAlchemyError as e:
            db.rollback()
            raise e

        return orden
