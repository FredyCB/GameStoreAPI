# routes/Inventario.py
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from utils.database import get_db
from schemas.Inventario import InventarioCreate, InventarioUpdate, InventarioResponse
from Controllers.Inventario_controller import InventarioController

router = APIRouter(prefix="/inventario", tags=["Inventario"])

@router.get("/", response_model=list[InventarioResponse])
def list_inv(db: Session = Depends(get_db)):
    return InventarioController.list_all(db)

@router.get("/{inv_id}", response_model=InventarioResponse)
def get_inv(inv_id: int, db: Session = Depends(get_db)):
    inv = InventarioController.get(db, inv_id)
    if not inv:
        raise HTTPException(status_code=404, detail="Inventario no encontrado")
    return inv

@router.post("/", response_model=InventarioResponse)
def create_inv(payload: InventarioCreate, db: Session = Depends(get_db)):
    try:
        return InventarioController.create(db, payload)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.put("/{inv_id}", response_model=InventarioResponse)
def update_inv(inv_id: int, payload: InventarioUpdate, db: Session = Depends(get_db)):
    try:
        inv = InventarioController.update(db, inv_id, payload)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
    if not inv:
        raise HTTPException(status_code=404, detail="Inventario no encontrado")
    return inv

@router.delete("/{inv_id}")
def delete_inv(inv_id: int, db: Session = Depends(get_db)):
    inv = InventarioController.delete(db, inv_id)
    if not inv:
        raise HTTPException(status_code=404, detail="Inventario no encontrado")
    return {"detail": "Entrada eliminada correctamente"}

