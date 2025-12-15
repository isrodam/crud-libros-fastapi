# app/main.py
from fastapi import FastAPI
from app.db.database import engine
from app.db.models import Base
from app.routers import editorial

# Función para crear las tablas al iniciar la API
def create_tables():
    # Base.metadata.create_all le dice a SQLAlchemy que cree todas las tablas
    # definidas en models.py
    Base.metadata.create_all(bind=engine)

# 1. Ejecutar la función de creación de tablas
create_tables()

app = FastAPI(title="API CRUD de Libros")

# 2. Incluir el router de editoriales
app.include_router(editorial.router, prefix="/editoriales", tags=["Editoriales"])

@app.get("/", tags=["Root"])
def read_root():
    return {"message": "Bienvenido a la API CRUD de Libros."}

# Para ejecutar: uvicorn app.main:app --reload