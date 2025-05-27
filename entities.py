from sqlalchemy import Column, Integer, String, DECIMAL, DateTime, ForeignKey
from sqlalchemy.sql import func
from forsit_admin_db import Base

class Product(Base):
    __tablename__ = 'product'
    p_id = Column(Integer, primary_key=True, index=True)
    p_name = Column(String(255), nullable=False)
    p_category = Column(String(100))
    p_price = Column(DECIMAL(10, 2), nullable=False)
    created_at = Column(DateTime, server_default=func.now())
    updated_at = Column(DateTime, server_default=func.now(), onupdate=func.now())

class Inventory(Base):
    __tablename__ = 'inventory'
    i_id = Column(Integer, primary_key=True, index=True)
    p_id = Column(Integer, ForeignKey("product.p_id"), nullable=False)
    i_quantity = Column(Integer, nullable=False)
    created_at = Column(DateTime, server_default=func.now())
    updated_at = Column(DateTime, server_default=func.now(), onupdate=func.now())

class Sale(Base):
    __tablename__ = 'sale'
    s_id = Column(Integer, primary_key=True, index=True)
    p_id = Column(Integer, ForeignKey("product.p_id"), nullable=False)
    s_quantity = Column(Integer, nullable=False)
    total_amount = Column(DECIMAL(10, 2), nullable=False)
    s_date = Column(DateTime, server_default=func.now())
    sales_channel = Column(String(50))

class InventoryLog(Base):
    __tablename__ = 'inventory_log'
    log_id = Column(Integer, primary_key=True, index=True)
    p_id = Column(Integer, ForeignKey("product.p_id"), nullable=False)
    change_type = Column(String(50), nullable=False)
    change_quantity = Column(Integer, nullable=False)
    new_stock = Column(Integer, nullable=False)
    changed_at = Column(DateTime, server_default=func.now())
