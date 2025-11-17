# routes/Juegos.py
from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.orm import Session
from utils.database import get_db
from schemas.Juego import JuegoCreate, JuegoUpdate, JuegoResponse
from Controllers.Juego_controller import JuegoController

router = APIRouter(prefix="/juegos", tags=["Juegos"])

@router.get("/", response_model=list[JuegoResponse])
def list_juegos(db: Session = Depends(get_db)):
    return JuegoController.list_all(db)

@router.get("/buscar_por_nombre", response_model=list[JuegoResponse])
def find_juego_nombre(nombre: str = Query(..., min_length=1), db: Session = Depends(get_db)):
    res = JuegoController.find_by_nombre(db, nombre)
    if not res:
        raise HTTPException(status_code=404, detail="No hay existencias")
    return res

@router.get("/por_inventario/{inventario_id}", response_model=JuegoResponse)
def get_por_inventario(inventario_id: int, db: Session = Depends(get_db)):
    j = JuegoController.get_by_inventario_id(db, inventario_id)
    if not j:
        raise HTTPException(status_code=404, detail="No hay existencias")
    return j

@router.post("/", response_model=JuegoResponse)
def create_juego(payload: JuegoCreate, db: Session = Depends(get_db)):
    try:
        return JuegoController.create(db, payload)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.put("/{juego_id}", response_model=JuegoResponse)
def update_juego(juego_id: int, payload: JuegoUpdate, db: Session = Depends(get_db)):
    try:
        j = JuegoController.update(db, juego_id, payload)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
    if not j:
        raise HTTPException(status_code=404, detail="Juego no encontrado")
    return j

@router.delete("/{juego_id}")
def delete_juego(juego_id: int, db: Session = Depends(get_db)):
    j = JuegoController.delete(db, juego_id)
    if not j:
        raise HTTPException(status_code=404, detail="Juego no encontrado")
    return {"detail": "Juego eliminado correctamente"}
