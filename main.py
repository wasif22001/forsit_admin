from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
import entities, schemas, crud
from forsit_admin_db import SessionLocal, engine, Base

Base.metadata.create_all(bind=engine)

app = FastAPI()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post("/products/", response_model=schemas.ProductOut)
def register_product(product: schemas.ProductCreate, db: Session = Depends(get_db)):
    return crud.create_product(db, product)

@app.get("/products/", response_model=list[schemas.ProductOut])
def list_products(db: Session = Depends(get_db)):
    return crud.get_all_products(db)
