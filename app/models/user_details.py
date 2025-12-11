from typing import Optional
import uuid
from sqlalchemy import ForeignKey, String, Enum
from sqlalchemy.orm import Mapped, mapped_column, relationship
from app.models.base import BaseModel
from app.models.users import Users


class UserDetails(BaseModel):
    __tablename__ = "user_details"
    
    name: Mapped[str] = mapped_column(String(100))
    surname: Mapped[str] = mapped_column(String(100))
    patronymic: Mapped[Optional[str]] = mapped_column(String(100), nullable=True)
    
    phone_number: Mapped[str] = mapped_column(String(11), unique=True)

    user_id: Mapped[uuid.UUID] = mapped_column(
        ForeignKey("users.id"),
        unique=True,
        nullable=False
    )
    user: Mapped["Users"] = relationship(
        back_populates="details"
    )


