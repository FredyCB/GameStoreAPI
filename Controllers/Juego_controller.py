from sqlalchemy.orm import Session
from models.Juego import Juego
from models.Inventario import Inventario


class JuegoController:

    @staticmethod
    def list_catalog(db: Session):
        """
        Retorna todos los juegos del inventario mostrando:
        id_inventario, nombre y precio
        """
        inventario_items = db.query(Inventario).all()

        return [
            {
                "inventario_id": item.id,
                "nombre": item.nombre,
                "precio": item.precio
            }
            for item in inventario_items
        ]

    @staticmethod
    def search(db: Session, nombre: str , inventario_id: int):
        """
        Busca por nombre del juego o por id_inventario.
        Si no existe devuelve None.
        """

        query = db.query(Inventario)

        if inventario_id:
            query = query.filter(Inventario.id == inventario_id)

        if nombre:
            query = query.filter(Inventario.nombre.ilike(f"%{nombre}%"))

        result = query.first()

        if not result:
            return None

        return {
            "inventario_id": result.id,
            "nombre": result.nombre,
            "precio": result.precio
        }
