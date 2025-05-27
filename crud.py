from sqlalchemy.orm import Session
import entities, schemas

def create_product(db: Session, product: schemas.ProductCreate):
    db_product = entities.Product(**product.dict())
    db.add(db_product)
    db.commit()
    db.refresh(db_product)
    return db_product

def get_all_products(db: Session):
    return db.query(entities.Product).all()
