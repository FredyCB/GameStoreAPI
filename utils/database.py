import os
from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

# Cargar variables del archivo .env
load_dotenv()

SQL_DRIVER = os.getenv("SQL_DRIVER")
SQL_SERVER = os.getenv("SQL_SERVER")
SQL_DATABASE = os.getenv("SQL_DATABASE")
SQL_USERNAME = os.getenv("SQL_USERNAME")
SQL_PASSWORD = os.getenv("SQL_PASSWORD")

# Construir la URL de conexión
DATABASE_URL = (
    "mssql+pyodbc://"
    f"{SQL_USERNAME}:{SQL_PASSWORD}"
    f"@{SQL_SERVER}:1433"
    f"/{SQL_DATABASE}"
    f"?driver={(SQL_DRIVER or '').replace(' ', '+')}"
)

# Crear el engine SQLAlchemy
engine = create_engine(
    DATABASE_URL,
    fast_executemany=True,
    echo=False
)

# Crear la sesión
SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)

# Clase base para los modelos
Base = declarative_base()

# Dependencia de sesión para FastAPI
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
