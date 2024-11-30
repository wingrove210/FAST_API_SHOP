from sqlalchemy.orm import Mapped, mapped_column, relationship
from datetime import datetime
from .base import Base
from sqlalchemy import func
from typing import Union, TYPE_CHECKING
from .order_product_association import OrderProductAssociation

if TYPE_CHECKING:
    from .product import Product
    from .order_product_association import OrderProductAssociation
class Order(Base):
    promocode: Mapped[Union[str, None]]
    # promocode: Mapped[str]
    created_at: Mapped[datetime] = mapped_column(
        server_default=func.now(),
        default=datetime.utcnow
    )
    products: Mapped[list["Product"]] = relationship(back_populates="orders", secondary="order_product_association")
    product_details: Mapped[list["OrderProductAssociation"]] = relationship(
        back_populates="parent"
    )
