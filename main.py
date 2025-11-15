from fastapi import FastAPI
from datetime import datetime
from routes import Clientes, Inventario, Juegos, Orden

app = FastAPI(title="GameStore API", json_encoders={
    datetime: lambda dt: dt.isoformat()
})

app.include_router(Clientes.router, prefix="/clientes", tags=["Clientes"])
app.include_router(Inventario.router, prefix="/inventario", tags=["Inventario"])
app.include_router(Juegos.router, prefix="/juegos", tags=["Juegos"])
app.include_router(Orden.router, prefix="/ordenes", tags=["Ordenes"])