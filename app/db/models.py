# app/db/models.py
from sqlalchemy import Column, Integer, String # <--- IMPORTACIONES CRÍTICAS
from sqlalchemy.orm import DeclarativeBase # <--- Base de modelos ORM

# Clase base de la que heredarán todos los modelos ORM
class Base(DeclarativeBase):
    pass

# Modelo ORM para la entidad Editorial
class Editorial(Base):
    __tablename__ = 'editoriales'
    
    # ¡Asegúrate de que las C de Column y las S de String sean MAYÚSCULAS!
    id = Column(Integer, primary_key=True, index=True) 
    nombre = Column(String, unique=True, index=True)
    pais = Column(String)
    
    # Comenta o elimina cualquier relación que aún no esté implementada
    # (ej. relación con Libros). Si no hay más modelos, déjalo limpio.