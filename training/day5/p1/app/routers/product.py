from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List
from ..crud import product as product_crud
from ..schemas.product import ProductCreate, ProductUpdate, ProductInDB
from ..db import get_db

router = APIRouter(prefix="/products", tags=["products"])

@router.post("/", response_model=ProductInDB, status_code=status.HTTP_201_CREATED)
def create_product(product: ProductCreate, db: Session = Depends(get_db)):
    return product_crud.create_product(db, product)

@router.get("/", response_model=List[ProductInDB])
def read_products(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return product_crud.get_products(db, skip=skip, limit=limit)

@router.get("/{product_id}", response_model=ProductInDB)
def read_product(product_id: int, db: Session = Depends(get_db)):
    product = product_crud.get_product(db, product_id)
    if product is None:
        raise HTTPException(status_code=404, detail="Product not found")
    return product

@router.put("/{product_id}", response_model=ProductInDB)
def update_product(product_id: int, product: ProductUpdate, db: Session = Depends(get_db)):
    updated_product = product_crud.update_product(db, product_id, product)
    if updated_product is None:
        raise HTTPException(status_code=404, detail="Product not found")
    return updated_product

@router.delete("/{product_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_product(product_id: int, db: Session = Depends(get_db)):
    success = product_crud.delete_product(db, product_id)
    if not success:
        raise HTTPException(status_code=404, detail="Product not found") 