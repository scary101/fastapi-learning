from typing import Optional, TYPE_CHECKING
import uuid
from sqlalchemy import ForeignKey, String, Enum
from sqlalchemy.orm import Mapped, mapped_column, relationship
from app.models.base import BaseModel

if TYPE_CHECKING:
    from app.models.user import User


class UserDetail(BaseModel):
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
    user: Mapped["User"] = relationship(
        back_populates="details"
    )


