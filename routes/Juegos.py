from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from utils.database import get_db

from Controllers.Juego_controller import JuegoController
from schemas.Juego import JuegoCreate, JuegoUpdate, JuegoResponse

router = APIRouter(prefix="/juegos", tags=["Juegos"])

@router.get("/", response_model=list[JuegoResponse])
def list_all(db: Session = Depends(get_db)):
    return JuegoController.list_all(db)

@router.post("/", response_model=JuegoResponse)
def create(payload: JuegoCreate, db: Session = Depends(get_db)):
    return JuegoController.create(db, payload)

@router.get("/{juego_id}", response_model=JuegoResponse)
def get(juego_id: int, db: Session = Depends(get_db)):
    obj = JuegoController.get_by_id(db, juego_id)
    if not obj:
        raise HTTPException(404, "Juego no encontrado")
    return obj

@router.put("/{juego_id}", response_model=JuegoResponse)
def update(juego_id: int, payload: JuegoUpdate, db: Session = Depends(get_db)):
    return JuegoController.update(db, juego_id, payload)

@router.delete("/{juego_id}", response_model=JuegoResponse)
def delete(juego_id: int, db: Session = Depends(get_db)):
    return JuegoController.delete(db, juego_id)

@router.get("/buscar", response_model=list[JuegoResponse])
def buscar(nombre: str, db: Session = Depends(get_db)):
    return JuegoController.find_by_nombre(db, nombre)

@router.get("/por_inventario/{inventario_id}", response_model=list[JuegoResponse])
def juegos_por_inventario(inventario_id: int, db: Session = Depends(get_db)):
    return JuegoController.get_by_inventario_id(db, inventario_id)
