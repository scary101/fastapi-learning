from typing import List
from sqlalchemy import String, null
from app.models.base import BaseModel
from sqlalchemy.orm import  Mapped, mapped_column, relationship
from app.models.category_characteristic import CategoryCharacteristic





class Characteristic(BaseModel):
    __tablename__ = "characteristics"
    
    name: Mapped[str] = mapped_column(String(50), nullable=False) 
    unit: Mapped[str] = mapped_column(String(10), nullable=False)
    
    category_characteristic: Mapped[List["CategoryCharacteristic"]] = relationship(
        "CategoryCharacteristic",
        back_populates="characteristic"
    )