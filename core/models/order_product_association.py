from sqlalchemy import Table, Column, ForeignKey, Integer, UniqueConstraint
from .base import Base
from sqlalchemy.orm import Mapped, mapped_column, relationship
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .order import Order
    from .product import Product
    
class OrderProductAssociation(Base):
    __tablename__ = "order_product_association"
    __table_args__ = (
    UniqueConstraint(
        "order_id",
        "product_id",
        name = "idx_unique_order_products",
        ),
    )
    id: Mapped[int] = mapped_column(primary_key=True)
    order_id: Mapped[int] = mapped_column(ForeignKey("orders.id"))
    product_id: Mapped[int] = mapped_column(ForeignKey("products.id"))
    count: Mapped[int] = mapped_column(default=1, server_default="1")
    
    child: Mapped["Order"] = relationship(back_populates="product_details")
    parent: Mapped["Product"] = relationship(back_populates="orders_details")
