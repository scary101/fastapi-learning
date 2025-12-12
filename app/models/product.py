from decimal import Decimal
from uuid import UUID

from sqlalchemy import ForeignKey, Numeric
from app.models.base import BaseModel
from sqlalchemy.orm import Mapped, mapped_column, relationship
from typing import Optional, TYPE_CHECKING

if TYPE_CHECKING:
    from app.models.category import Category
    from app.models.entrepreneur import Entrepreneur


class Product(BaseModel):
    __tablename__ = "products"
    
    category_id: Mapped[UUID] = mapped_column(
        ForeignKey("categories.id"),
        nullable=False
    )
    category: Mapped["Category"] = relationship(
        "Category",
        back_populates="products"
    )
    entrepreneur_id: Mapped[UUID] = mapped_column(
        ForeignKey("entrepreneurs.id"),
        nullable=False
    )
    entrepreneur: Mapped["Entrepreneur"] = relationship(
        "Entrepreneur",
        back_populates="products"
    )
    
    description: Mapped[Optional[str]] = mapped_column()
    price: Mapped[Decimal] = mapped_column(Numeric(10, 2), nullable=False)
    stock: Mapped[int] = mapped_column(nullable=False, default=0)
    reviews_count: Mapped[Optional[int]] = mapped_column(default=0, nullable=True)
    rating: Mapped[Optional[Decimal]] = mapped_column(nullable=True)
    photo_path: Mapped[Optional[str]] = mapped_column()
    

