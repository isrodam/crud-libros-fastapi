# app/db/models.py
from sqlalchemy import Column, Integer, String, Date, Float, ForeignKey, Table
from sqlalchemy.orm import relationship, DeclarativeBase

# Clase base de la que heredarán todos los modelos ORM
class Base(DeclarativeBase):
    pass

# Modelo ORM para la entidad Editorial
class Editorial(Base):
    __tablename__ = 'editoriales'
    
    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String, unique=True, index=True)
    pais = Column(String)
    
    # 🔗 Relación con Libros (Relación 1:N)
    # Esto es una lista de objetos Libro asociados a esta editorial
    libros = relationship("Libro", back_populates="editorial")