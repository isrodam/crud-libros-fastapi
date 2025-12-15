# app/schemas/editorial.py
from pydantic import BaseModel, Field
from typing import Optional

# 1. Esquema Base (Creación / Actualización)
# Define la estructura mínima de datos que un cliente enviará al crear o actualizar
class EditorialBase(BaseModel):
    # nombre y país son obligatorios para crear una editorial
    nombre: str = Field(..., min_length=2, max_length=100, description="Nombre de la editorial")
    pais: str = Field(..., min_length=2, max_length=50, description="País de origen de la editorial")

# 2. Esquema de Creación (Input)
# En este caso, es idéntico al Base, pero se usa para claridad
class EditorialCreate(EditorialBase):
    pass # No necesitamos campos adicionales para la creación

# 3. Esquema de Salida (Output / Read)
# Define cómo se verán los datos cuando los enviemos de vuelta al cliente (Operación R)
class Editorial(EditorialBase):
    id: int # El ID es generado por la BBDD, por eso solo va en la salida
    
    # Configuración interna para que Pydantic pueda leer objetos de SQLAlchemy
    class Config:
        from_attributes = True