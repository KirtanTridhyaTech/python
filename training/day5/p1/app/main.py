from fastapi import FastAPI
from .routers import product, category
from .config import settings
from .db import engine, Base

# Create database tables
Base.metadata.create_all(bind=engine)

app = FastAPI(title="E-commerce API")

# Include routers
app.include_router(product.router, prefix=settings.API_V1_STR)
app.include_router(category.router, prefix=settings.API_V1_STR)

@app.get("/")
def read_root():
    return {"message": "Welcome to E-commerce API"} 