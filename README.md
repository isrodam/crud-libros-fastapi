Guía de todo el proceso de creación de API CRUD-Libros-FastAPI, desde la inicialización del proyecto hasta la prueba final.
________________________________________
📘 Guía Completa: Creación de API CRUD con FastAPI y SQLAlchemy
Este proceso está dividido en 33 pasos que cubren la configuración del entorno, la arquitectura del proyecto, la implementación del código y la depuración final.
I. 🚀 Etapa 1: Configuración Inicial del Proyecto (Pasos 1-6)
Paso	Acción	Comando / Resultado
1.	Creación de Carpeta	Crea la carpeta raíz del proyecto: C:\documents\projects\crud-libros-fastapi
2.	Inicialización de Git	Abre la terminal de PowerShell en esa carpeta e inicializa Git: git init
3.	Creación del Entorno Virtual	Crea el entorno virtual llamado venv: python -m venv venv
4.	Activación del Entorno	Activa el entorno virtual: .\venv\Scripts\Activate.ps1
5.	Instalación de Librerías	Instala todas las dependencias principales: pip install fastapi uvicorn "sqlalchemy[asyncio]" pydantic python-dotenv
6.	Creación de Carpeta de Aplicación	Crea la estructura base del código: mkdir app
II. 🏗️ Etapa 2: Estructura y Dependencias (Pasos 7-12)
Se crea la estructura de carpetas y los archivos de configuración iniciales.
Paso	Archivo	Código Clave
7.	.gitignore	Excluye el entorno virtual: venv/
8.	requirements.txt	Genera la lista de dependencias: pip freeze > requirements.txt
9.	.env (o env)	Configuración de Conexión. Contiene la URL de la base de datos (SQLite): DATABASE_URL=sqlite:///./app/database.db
10.	app/main.py	Punto de Entrada. Crea la instancia de FastAPI y la ruta raíz: app = FastAPI(title="API CRUD de Libros")
11.	app/db/database.py	Conexión a DB. Configura SQLAlchemy, lee .env y define la sesión: (Ver código abajo)
12.	app/db/models.py	Modelo ORM Base. Define la clase Base para heredar modelos. (Ver código abajo)
🔑 Código Clave: app/db/database.py
Python
# app/db/database.py
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, Session
from dotenv import load_dotenv
import os

load_dotenv()
SQLALCHEMY_DATABASE_URL = os.getenv("DATABASE_URL")

engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
III. 🏛️ Etapa 3: Definición de Esquemas y Modelos (Pasos 13-17)
Se definen las estructuras de datos que se usan para la base de datos (SQLAlchemy) y la validación (Pydantic).
Paso	Archivo	Código Clave (Editorial Model)
13.	app/db/models.py (Actualización)	Definición de Tabla. Se añade el modelo ORM: class Editorial(Base): __tablename__ = 'editoriales' id = Column(Integer, primary_key=True, index=True) nombre = Column(String, unique=True, index=True) pais = Column(String)
14.	app/schemas/editorial.py	Esquema Base (CREATE). Define la entrada de datos: class EditorialCreate(BaseModel): nombre: str pais: str
15.	app/schemas/editorial.py	Esquema de Salida (READ). Define la salida de datos (incluyendo el ID): class Editorial(EditorialBase): id: int class Config: from_attributes = True
16.	app/schemas/editorial.py	Esquema de Actualización (UPDATE). Define la entrada para el PUT: class EditorialUpdate(EditorialBase): pass
17.	app/main.py (Actualización)	Función de Creación de Tablas. Se añade la función para crear la base de datos al inicio: def create_tables(): Base.metadata.create_all(bind=engine) y se llama a create_tables().
IV. 🛠️ Etapa 4: Lógica de Negocio y Enrutamiento (Pasos 18-24)
Se implementan las funciones CRUD reales y se enlazan a la API.
Paso	Archivo	Código Clave
18.	app/services/editorial.py	Función CREATE. Lógica para crear un registro: db_editorial = models.Editorial(...) db.add(db_editorial); db.commit()
19.	app/services/editorial.py	Función READ (by ID). Lógica para obtener un registro por ID: db.query(models.Editorial).filter(models.Editorial.id == editorial_id).first()
20.	app/services/editorial.py	Función READ (all). Lógica para listar todos los registros: db.query(models.Editorial).all()
21.	app/services/editorial.py	Función UPDATE. Lógica para actualizar un registro: for key, value in editorial.model_dump().items(): setattr(db_editorial, key, value)
22.	app/services/editorial.py	Función DELETE. Lógica para eliminar un registro: db.delete(db_editorial); db.commit()
23.	app/routers/editorial.py	Definición de Router. Se crea el Blueprint de la API: router = APIRouter(prefix="/editoriales", tags=["Editoriales"])
24.	app/routers/editorial.py	Endpoints CRUD. Se definen los endpoints (POST, GET, PUT, DELETE) inyectando la dependencia de base de datos (Depends(get_db)).
V. 🔗 Etapa 5: Enlace Final y Puesta en Marcha (Pasos 25-28)
Se completa la conexión de los routers y se prepara el servidor.
Paso	Acción	Comando / Resultado
25.	Incluir el Router	Se importa el router en app/main.py: app.include_router(editorial.router)
26.	Configurar Archivos (Depuración)	Se corrige el error de inicialización asegurando que .env esté bien nombrado y que models.py sea sintácticamente correcto.
27.	Ejecución Inicial	Se inicia el servidor (intento fallido en el puerto 8000): uvicorn app.main:app --reload
28.	Depuración de Puerto	Se resuelve el conflicto de puerto (que causaba que el navegador no cargara) ejecutando en el puerto 8001: uvicorn app.main:app --reload --port 8001
VI. ✅ Etapa 6: Pruebas Funcionales Finales (Pasos 29-33)
Con el servidor estable en http://127.0.0.1:8001, se realizaron las pruebas cruciales en la documentación de Swagger UI.
Paso	Operación	Endpoint y Datos	Código de Éxito
29.	CREATE	POST /editoriales/ con {"nombre": "Planeta", "pais": "España"}	201 Created (Devuelve ID 1)
30.	READ	GET /editoriales/1	200 Successful (Devuelve el objeto)
31.	UPDATE	PUT /editoriales/1 con {"pais": "Argentina"}	200 Successful (Registro modificado)
32.	DELETE	DELETE /editoriales/1	204 No Content (Registro eliminado)
33.	Sincronización	Se suben todos los cambios a GitHub: git add ., git commit -m "feat: CRUD Editorial completo", git push	
________________________________________
Este es el proceso completo ejecutado para construir la API. 
A continuación, el código completo de los archivos clave.
________________________________________
💻 Código Completo Final del Proyecto CRUD-Libros-FastAPI
Este es el código que debe funcionar correctamente cuando se ejecuta en el puerto 8001.
1. app/db/database.py (Conexión a la Base de Datos)
Este archivo configura la conexión con el motor SQLite y la sesión que se utiliza en la lógica de servicios.
Python
# app/db/database.py
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, Session
from dotenv import load_dotenv
import os

# Carga la variable de entorno desde .env
load_dotenv()
SQLALCHEMY_DATABASE_URL = os.getenv("DATABASE_URL")

# Crea el motor de la base de datos (SQLite en este caso)
# 'connect_args' es necesario para SQLite en FastAPI/SQLAlchemy
engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
)

# Configura la fábrica de sesiones (SessionLocal)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Dependencia para obtener la sesión de la base de datos
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
2. app/db/models.py (Modelos ORM de SQLAlchemy)
Define la estructura de las tablas de la base de datos.
Python
# app/db/models.py
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import DeclarativeBase

# Clase Base de la que heredarán todos los modelos ORM
class Base(DeclarativeBase):
    pass

# Modelo ORM para la entidad Editorial
class Editorial(Base):
    __tablename__ = 'editoriales'
    
    # Columnas de la tabla
    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String, unique=True, index=True)
    pais = Column(String)
3. app/schemas/editorial.py (Esquemas Pydantic)
Define la estructura de datos para la validación de entrada/salida de la API.
Python
# app/schemas/editorial.py
from pydantic import BaseModel

# Esquema Base para datos comunes (usado en CREATE y UPDATE)
class EditorialBase(BaseModel):
    nombre: str
    pais: str

# Esquema para la creación de una editorial (entrada de datos POST)
class EditorialCreate(EditorialBase):
    pass

# Esquema para la actualización de una editorial (entrada de datos PUT)
class EditorialUpdate(EditorialBase):
    pass

# Esquema para la lectura/respuesta de una editorial (salida de datos)
class Editorial(EditorialBase):
    id: int
    
    # Permite que el modelo Pydantic lea datos de un objeto ORM
    class Config:
        from_attributes = True 
4. app/services/editorial.py (Lógica de Negocio/Servicios)
Contiene todas las operaciones CRUD que interactúan con la base de datos (usando la sesión db).
Python
# app/services/editorial.py
from sqlalchemy.orm import Session
from app.db import models
from app.schemas import editorial as schemas

# ----------------- CREATE -----------------
def create_editorial(db: Session, editorial: schemas.EditorialCreate):
    db_editorial = models.Editorial(
        nombre=editorial.nombre, 
        pais=editorial.pais
    )
    db.add(db_editorial)
    db.commit()
    db.refresh(db_editorial)
    return db_editorial

# ----------------- READ -----------------
def get_editorial(db: Session, editorial_id: int):
    return db.query(models.Editorial).filter(models.Editorial.id == editorial_id).first()

def get_editoriales(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Editorial).offset(skip).limit(limit).all()

# ----------------- UPDATE -----------------
def update_editorial(db: Session, db_editorial: models.Editorial, editorial: schemas.EditorialUpdate):
    for key, value in editorial.model_dump(exclude_unset=True).items():
        setattr(db_editorial, key, value)
    
    db.commit()
    db.refresh(db_editorial)
    return db_editorial

# ----------------- DELETE -----------------
def delete_editorial(db: Session, editorial_id: int):
    db_editorial = db.query(models.Editorial).filter(models.Editorial.id == editorial_id).first()
    if db_editorial:
        db.delete(db_editorial)
        db.commit()
    return db_editorial
5. app/routers/editorial.py (Endpoints de la API)
Define las rutas HTTP y llama a la capa de servicios.
Python
# app/routers/editorial.py
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List

from app.db.database import get_db
from app.schemas import editorial as schemas
from app.services import editorial as services

router = APIRouter(
    prefix="/editoriales",
    tags=["Editoriales"]
)

# ----------------- CREATE (POST) -----------------
@router.post("/", response_model=schemas.Editorial, status_code=status.HTTP_201_CREATED)
def create_editorial(editorial: schemas.EditorialCreate, db: Session = Depends(get_db)):
    return services.create_editorial(db=db, editorial=editorial)

# ----------------- READ (GET All) -----------------
@router.get("/", response_model=List[schemas.Editorial])
def read_editoriales(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    editoriales = services.get_editoriales(db, skip=skip, limit=limit)
    return editoriales

# ----------------- READ (GET by ID) -----------------
@router.get("/{editorial_id}", response_model=schemas.Editorial)
def read_editorial(editorial_id: int, db: Session = Depends(get_db)):
    db_editorial = services.get_editorial(db, editorial_id=editorial_id)
    if db_editorial is None:
        raise HTTPException(status_code=404, detail="Editorial no encontrada")
    return db_editorial

# ----------------- UPDATE (PUT) -----------------
@router.put("/{editorial_id}", response_model=schemas.Editorial)
def update_editorial(editorial_id: int, editorial: schemas.EditorialUpdate, db: Session = Depends(get_db)):
    db_editorial = services.get_editorial(db, editorial_id=editorial_id)
    if db_editorial is None:
        raise HTTPException(status_code=404, detail="Editorial no encontrada")
    return services.update_editorial(db, db_editorial=db_editorial, editorial=editorial)

# ----------------- DELETE (DELETE) -----------------
@router.delete("/{editorial_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_editorial(editorial_id: int, db: Session = Depends(get_db)):
    db_editorial = services.get_editorial(db, editorial_id=editorial_id)
    if db_editorial is None:
        raise HTTPException(status_code=404, detail="Editorial no encontrada")
    services.delete_editorial(db, editorial_id=editorial_id)
    return {"ok": True}
6. app/main.py (Punto de Entrada de la Aplicación)
El archivo principal que inicializa FastAPI, crea las tablas y enlaza el router.
Python
# app/main.py
from fastapi import FastAPI
from app.db.database import engine
from app.db.models import Base
from app.routers import editorial

# Función para crear las tablas al iniciar la API
def create_tables():
    # Base.metadata.create_all le dice a SQLAlchemy que cree todas las tablas
    # definidas en models.py (Crucial para inicializar la DB)
    Base.metadata.create_all(bind=engine)

# 1. Ejecutar la función de creación de tablas
create_tables()

# 2. Inicializar la aplicación FastAPI
app = FastAPI(title="API CRUD de Libros")

# 3. Ruta principal de bienvenida
@app.get("/")
def home():
    return {"message": "Bienvenido a la API CRUD de Libros."}

# 4. Incluir el router de la entidad Editorial
app.include_router(editorial.router)
