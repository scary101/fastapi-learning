from uuid import UUID

from sqlalchemy import ForeignKey, String
from app.models.base import BaseModel
from sqlalchemy.orm import Mapped, mapped_column, relationship
from typing import List, Optional, Text, TYPE_CHECKING
from app.models.product import Product


if TYPE_CHECKING:
    from app.models.user import User
    from app.models.wallet import Wallet



class Entrepreneur(BaseModel):
    __tablename__ = "entrepreneurs"
    
    user_id: Mapped[UUID] = mapped_column(
        ForeignKey("users.id"),
        unique=True
    )
    user: Mapped["User"] = relationship(
        back_populates="ep_info"
    )
    wallet: Mapped["Wallet"] = relationship(
        back_populates="entrepreneur",
        uselist=False
    )
    account_number: Mapped[str] = mapped_column(String(30), nullable=False)
    inn: Mapped[str] = mapped_column(String(12), nullable=False)
    short_name: Mapped[str] = mapped_column(String(100), nullable=False)
    bik: Mapped[str] = mapped_column(String(9), nullable=False)
    full_name: Mapped[str] = mapped_column(String(255), nullable=False)
    ogrnip: Mapped[str] = mapped_column(String(15), nullable=False)
    legal_adress: Mapped[str] = mapped_column(String(350), nullable=False)
    magazine_name: Mapped[str] = mapped_column(String(100), nullable=False)
    
    
    products: Mapped[List["Product"]] = relationship(
        back_populates="entrepreneur"
    )
    
    
    
