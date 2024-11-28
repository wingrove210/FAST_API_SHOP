from typing import TYPE_CHECKING, Union
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import String, ForeignKey

from .base import Base
from .mixins import UserRelationMixin

if TYPE_CHECKING:
    from .user import User


class Profile(UserRelationMixin, Base):
    _user_id_unique = False
    _user_back_populates = "profile"
    first_name: Mapped[Union[str, None]] = mapped_column(String(40))
    last_name: Mapped[Union[str, None]] = mapped_column(String(40))
    bio: Mapped[Union[str, None]]

