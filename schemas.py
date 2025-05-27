from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class ProductCreate(BaseModel):
    p_name: str
    p_category: Optional[str]
    p_price: float

class ProductOut(ProductCreate):
    p_id: int
    created_at: datetime
    updated_at: datetime

    class Config:
        orm_mode = True
