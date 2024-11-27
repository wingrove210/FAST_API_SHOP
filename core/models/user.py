from typing import TYPE_CHECKING
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import String

from .base import Base

if TYPE_CHECKING:
    from .post import Post

class User(Base):
    username: Mapped[str] = mapped_column(String(32), unique=True)

    post: Mapped[list["Post"]] = relationship(back_populates="user")
