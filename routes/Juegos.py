from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from utils.database import get_db
from Controllers.Juego_controller import JuegoController
from schemas.Juego import JuegoCatalogoResponse, JuegoSearchResponse

router = APIRouter()
    

@router.get("/", response_model=list[JuegoCatalogoResponse])
def listar_juegos(db: Session = Depends(get_db)):
    return JuegoController.list_catalog(db)


@router.get("/buscar", response_model=JuegoSearchResponse)
def buscar_juego(
    nombre: str | None = None,
    inventario_id: int | None = None,
    db: Session = Depends(get_db)
):
    if not nombre and not inventario_id:
        raise HTTPException(400, "Debe enviar nombre o inventario_id")

    result = JuegoController.search(db, nombre, inventario_id)

    if not result:
        raise HTTPException(404, "No hay existencias")

    return result
