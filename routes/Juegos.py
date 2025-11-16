# routes/Juegos.py
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from utils.database import get_db
from schemas.Juego import JuegoCreate, JuegoResponse
from Controllers.Juego_controller import JuegoController

router = APIRouter()

@router.get("/", response_model=list[JuegoResponse])
def list_juegos(db: Session = Depends(get_db)):
    return JuegoController.list_all(db)

@router.get("/{juego_id}", response_model=JuegoResponse)
def get_juego(juego_id: int, db: Session = Depends(get_db)):
    juego = JuegoController.get(db, juego_id)
    if not juego:
        raise HTTPException(status_code=404, detail="Juego not found")
    return juego

@router.post("/", response_model=JuegoResponse, status_code=201)
def create_juego(payload: JuegoCreate, db: Session = Depends(get_db)):
    return JuegoController.create(db, payload)

@router.put("/{juego_id}", response_model=JuegoResponse)
def update_juego(juego_id: int, payload: JuegoCreate, db: Session = Depends(get_db)):
    juego = JuegoController.update(db, juego_id, payload)
    if not juego:
        raise HTTPException(status_code=404, detail="Juego not found")
    return juego

@router.delete("/{juego_id}")
def delete_juego(juego_id: int, db: Session = Depends(get_db)):
    res = JuegoController.delete(db, juego_id)
    if not res:
        raise HTTPException(status_code=404, detail="Juego not found")
    return {"detail": "deleted"}
