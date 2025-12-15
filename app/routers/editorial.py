# app/routers/editorial.py
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.db.database import get_db
from app.schemas import editorial as schemas
from app.services import editorial as services

router = APIRouter()

# CREATE (POST)
@router.post(
    "/",
    response_model=schemas.Editorial,
    status_code=status.HTTP_201_CREATED,
    summary="Crea una nueva editorial"
)
def crear_editorial(
    editorial: schemas.EditorialCreate,
    db: Session = Depends(get_db)
):
    db_editorial = services.create_editorial(db=db, editorial=editorial)
    return db_editorial

# READ (GET - Todos)
@router.get(
    "/",
    response_model=list[schemas.Editorial],
    summary="Obtiene la lista de todas las editoriales"
)
def leer_editoriales(
    skip: int = 0, limit: int = 100,
    db: Session = Depends(get_db)
):
    editoriales = services.get_editoriales(db, skip=skip, limit=limit)
    return editoriales

# READ (GET - Por ID)
@router.get(
    "/{editorial_id}",
    response_model=schemas.Editorial,
    summary="Obtiene una editorial por su ID"
)
def leer_editorial_por_id(
    editorial_id: int,
    db: Session = Depends(get_db)
):
    db_editorial = services.get_editorial(db, editorial_id=editorial_id)
    if db_editorial is None:
        raise HTTPException(
            status_code=404, detail="Editorial no encontrada"
        )
    return db_editorial

# UPDATE (PUT)
@router.put(
    "/{editorial_id}",
    response_model=schemas.Editorial,
    summary="Actualiza una editorial existente por su ID"
)
def actualizar_editorial(
    editorial_id: int,
    editorial_data: schemas.EditorialUpdate,
    db: Session = Depends(get_db)
):
    updated_editorial = services.update_editorial(
        db=db, 
        editorial_id=editorial_id, 
        editorial_data=editorial_data
    )
    if updated_editorial is None:
        raise HTTPException(
            status_code=404, detail="Editorial no encontrada para actualizar"
        )
    return updated_editorial

# DELETE (DELETE)
@router.delete(
    "/{editorial_id}",
    status_code=status.HTTP_204_NO_CONTENT,
    summary="Elimina una editorial por su ID"
)
def eliminar_editorial(
    editorial_id: int,
    db: Session = Depends(get_db)
):
    db_editorial = services.delete_editorial(db=db, editorial_id=editorial_id)
    if db_editorial is None:
        raise HTTPException(
            status_code=404, detail="Editorial no encontrada para eliminar"
        )
    return