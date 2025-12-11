from decimal import Decimal
from uuid import UUID

from sqlalchemy import ForeignKey, Numeric
from app.models.base import BaseModel
from sqlalchemy.orm import Mapped, mapped_column, relationship
from app.models.entrepreneurs import Entrepreneurs



class Wallets(BaseModel):
    balance: Mapped[Decimal] = mapped_column(Numeric(10, 2), default=0, nullable=True)
    entrepreneur_id: Mapped[UUID] = mapped_column(
        ForeignKey("entrepreneurs.id"),
        unique=True
    )
    entrepreneur: Mapped["Entrepreneurs"] = relationship(
        back_populates="wallet",
        uselist=False
    )