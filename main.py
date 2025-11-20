# main.py
import uvicorn
from fastapi import FastAPI
from datetime import datetime

# Importacion de los routers
from routes.Clientes import router as clientes_router
from routes.Inventario import router as inventarios_router
from routes.Juegos import router as juegos_router
from routes.Orden import router as ordenes_router

app = FastAPI(
    title="GameStore API",
    json_encoders={datetime: lambda dt: dt.isoformat()},
)

# Registrar los routers en la API
app.include_router(clientes_router, prefix="/clientes", tags=["Clientes"])
app.include_router(inventarios_router, prefix="/inventarios", tags=["Inventarios"])
app.include_router(juegos_router, prefix="/juegos", tags=["Juegos"])
app.include_router(ordenes_router, prefix="/ordenes", tags=["Ordenes"])

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
