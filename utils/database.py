import os
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv
from urllib.parse import quote_plus

load_dotenv()

DRIVER = os.getenv('AZURE_SQL_DRIVER', 'ODBC Driver 17 for SQL Server')
SERVER = os.getenv('AZURE_SQL_SERVER', 'your_server.database.windows.net')
DATABASE = os.getenv('AZURE_SQL_DATABASE', 'your_db')
UID = os.getenv('AZURE_SQL_UID', 'user')
PWD = os.getenv('AZURE_SQL_PWD', 'pwd')

odbc_str = f"DRIVER={{{DRIVER}}};SERVER={SERVER};DATABASE={DATABASE};UID={UID};PWD={PWD};Encrypt=yes;TrustServerCertificate=no"
params = quote_plus(odbc_str)
SQLALCHEMY_DATABASE_URL = f"mssql+pyodbc:///?odbc_connect={params}"

engine = create_engine(SQLALCHEMY_DATABASE_URL, fast_executemany=True)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
