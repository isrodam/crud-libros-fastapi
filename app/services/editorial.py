# app/services/editorial.py
from sqlalchemy.orm import Session
from app.db import models
from app.schemas import editorial as schemas

# C - CREATE
def create_editorial(db: Session, editorial: schemas.EditorialCreate):
    db_editorial = models.Editorial(
        nombre=editorial.nombre, 
        pais=editorial.pais
    )
    db.add(db_editorial)
    db.commit()
    db.refresh(db_editorial)
    return db_editorial

# R - READ (Por ID)
def get_editorial(db: Session, editorial_id: int):
    return db.query(models.Editorial).filter(models.Editorial.id == editorial_id).first()

# R - READ (Todos)
def get_editoriales(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Editorial).offset(skip).limit(limit).all()

# U - UPDATE
def update_editorial(db: Session, editorial_id: int, editorial_data: schemas.EditorialUpdate):
    db_editorial = get_editorial(db, editorial_id)
    if db_editorial is None:
        return None
        
    # Actualizar campos solo si se proporcionaron
    if editorial_data.nombre is not None:
        db_editorial.nombre = editorial_data.nombre
    if editorial_data.pais is not None:
        db_editorial.pais = editorial_data.pais
        
    db.commit()
    db.refresh(db_editorial)
    
    return db_editorial

# D - DELETE
def delete_editorial(db: Session, editorial_id: int):
    db_editorial = get_editorial(db, editorial_id)
    if db_editorial is None:
        return None
        
    db.delete(db_editorial)
    db.commit()
    
    return db_editorial