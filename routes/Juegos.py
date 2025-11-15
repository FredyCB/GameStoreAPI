from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.orm import Session
from utils.database import get_db
from schemas.Juego import JuegoCreate, JuegoResponse
from Controllers.Juego_controller import JuegoController

router = APIRouter()

@router.get("/by-inventario/{inventario_id}", response_model=list[JuegoResponse])
def list_by_inv(inventario_id: int, db: Session = Depends(get_db)):
    return JuegoController.list_by_inventario(db, inventario_id)

@router.get("/{juego_id}", response_model=JuegoResponse)
def get_juego(juego_id: int, db: Session = Depends(get_db)):
    j = JuegoController.get(db, juego_id)
    if not j:
        raise HTTPException(404, "Juego not found")
    return j

@router.post("/", response_model=JuegoResponse)
def create_juego(payload: JuegoCreate, db: Session = Depends(get_db)):
    return JuegoController.create(db, payload)

@router.delete("/{juego_id}")
def delete_juego(juego_id: int, db: Session = Depends(get_db)):
    res = JuegoController.delete(db, juego_id)
    if not res:
        raise HTTPException(404, "Juego not found")
    return {"detail": "deleted"}
