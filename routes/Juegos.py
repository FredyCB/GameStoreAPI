from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from utils.database import get_db
from schemas.Juego import JuegoCreate, JuegoUpdate, JuegoResponse
from Controllers.Juego_controller import JuegoController

router = APIRouter()

@router.get("/", response_model=list[JuegoResponse])
def list_juegos(db: Session = Depends(get_db)):
    return JuegoController.list_all(db)

@router.get("/{juego_id}", response_model=JuegoResponse)
def get_juego(juego_id: int, db: Session = Depends(get_db)):
    j = JuegoController.get(db, juego_id)
    if not j:
        raise HTTPException(404, "Juego not found")
    return j

@router.post("/", response_model=JuegoResponse)
def create_juego(payload: JuegoCreate, db: Session = Depends(get_db)):
    return JuegoController.create(db, payload)

@router.put("/{juego_id}", response_model=JuegoResponse)
def update_juego(juego_id: int, payload: JuegoUpdate, db: Session = Depends(get_db)):
    j = JuegoController.update(db, juego_id, payload)
    if not j:
        raise HTTPException(404, "Juego not found")
    return j

@router.delete("/{juego_id}")
def delete_juego(juego_id: int, db: Session = Depends(get_db)):
    j = JuegoController.delete(db, juego_id)
    if not j:
        raise HTTPException(404, "Juego not found")
    return {"detail": "deleted"}
