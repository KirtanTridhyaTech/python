from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List
from ..crud import category as category_crud
from ..schemas.category import CategoryCreate, CategoryUpdate, CategoryInDB
from ..db import get_db

router = APIRouter(prefix="/categories", tags=["categories"])

@router.post("/", response_model=CategoryInDB, status_code=status.HTTP_201_CREATED)
def create_category(category: CategoryCreate, db: Session = Depends(get_db)):
    return category_crud.create_category(db, category)

@router.get("/", response_model=List[CategoryInDB])
def read_categories(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return category_crud.get_categories(db, skip=skip, limit=limit)

@router.get("/{category_id}", response_model=CategoryInDB)
def read_category(category_id: int, db: Session = Depends(get_db)):
    category = category_crud.get_category(db, category_id)
    if category is None:
        raise HTTPException(status_code=404, detail="Category not found")
    return category

@router.put("/{category_id}", response_model=CategoryInDB)
def update_category(category_id: int, category: CategoryUpdate, db: Session = Depends(get_db)):
    updated_category = category_crud.update_category(db, category_id, category)
    if updated_category is None:
        raise HTTPException(status_code=404, detail="Category not found")
    return updated_category

@router.delete("/{category_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_category(category_id: int, db: Session = Depends(get_db)):
    success = category_crud.delete_category(db, category_id)
    if not success:
        raise HTTPException(status_code=404, detail="Category not found") 