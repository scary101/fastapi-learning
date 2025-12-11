from sqlalchemy import String
from sqlalchemy import Enum as SQLEnum
from app.models.base import BaseModel
from sqlalchemy.orm import Mapped, mapped_column, relationship
from app.models.user_details import UserDetails
from app.models.enums.role_enum import Role
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from app.models.entrepreneurs import Entrepreneurs


class Users(BaseModel):
    __tablename__ = "users"
    email: Mapped[str] = mapped_column(String(100), unique=True)
    password: Mapped[str] = mapped_column(String, nullable=False)
    
    role: Mapped[Role] = mapped_column(
        SQLEnum(Role, name="role_enum"),
        default=Role.USER
    )
    is_active: Mapped[bool] = mapped_column(default=True)
    is_ep: Mapped[bool] = mapped_column(default=False)
    
    details: Mapped["UserDetails"] = relationship(
        back_populates="user",
        uselist=False
    )
    ep_info: Mapped["Entrepreneurs"] = relationship(
        back_populates="user",
        uselist=False
    )
    