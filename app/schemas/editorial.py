# app/schemas/editorial.py
from pydantic import BaseModel, Field
from typing import Optional

# 1. Esquema Base (Campos comunes)
class EditorialBase(BaseModel):
    nombre: str = Field(..., min_length=2, max_length=100, description="Nombre de la editorial")
    pais: str = Field(..., min_length=2, max_length=50, description="País de origen de la editorial")

# 2. Esquema de Creación (Input)
class EditorialCreate(EditorialBase):
    pass

# 3. Esquema de Actualización (PUT input - campos opcionales)
class EditorialUpdate(EditorialBase):
    nombre: Optional[str] = Field(None, min_length=2, max_length=100, description="Nombre opcional")
    pais: Optional[str] = Field(None, min_length=2, max_length=50, description="País opcional")

# 4. Esquema de Salida (GET/POST/PUT output - incluye ID)
class Editorial(EditorialBase):
    id: int
    class Config:
        from_attributes = True