from uuid import UUID

from sqlalchemy import ForeignKey, String
from app.models.base import BaseModel
from sqlalchemy.orm import Mapped, mapped_column, relationship
from typing import List, Optional
from app.models.category_characteristic import CategoryCharacteristic
from app.models.product import Product


class Category(BaseModel):
    __tablename__ = "categories"
    
    name: Mapped[str] = mapped_column(String(50), nullable=False)
    parent_id: Mapped[Optional[UUID]] = mapped_column(
        ForeignKey("categories.id"),
        nullable=True
    )
    parent: Mapped[Optional["Category"]] = relationship(
        "Category",
        remote_side="Category.id",
        back_populates="child"
    )
    child: Mapped[List["Category"]] = relationship(
        "Category",
        back_populates="parent"
    )
    
    characteristic_category: Mapped[List["CategoryCharacteristic"]] = relationship(
        "CategoryCharacteristic",
        back_populates="category"
    )
    
    products: Mapped[List["Product"]] = relationship(
        "Product",
        back_populates="category"
    )