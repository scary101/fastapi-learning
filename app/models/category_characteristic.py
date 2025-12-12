from uuid import UUID

from sqlalchemy import ForeignKey
from app.models.base import BaseModel
from sqlalchemy.orm import Mapped, mapped_column, relationship
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from app.models.category import Category
    from app.models.characteristic import Characteristic


class CategoryCharacteristic(BaseModel):
    __tablename__ = "category_characteristics"
     
    category_id: Mapped[UUID] = mapped_column(
        ForeignKey("categories.id"),
        nullable=False
    )
    category: Mapped["Category"] = relationship(
        "Category",
        back_populates="characteristic_category"
    )
    
    characteristic_id: Mapped[UUID] = mapped_column(
        ForeignKey("characteristics.id"),
        nullable=False
    )
    characteristic: Mapped["Characteristic"] = relationship(
        "Characteristic.id",
        back_populates="category_characteristic"
    )