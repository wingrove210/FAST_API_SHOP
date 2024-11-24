from pydantic import BaseModel, ConfigDict
from typing import Union


class ProductBase(BaseModel):
    name: str
    description: str
    price: int
    size: int


class ProductCreate(ProductBase):
    pass


class ProductUpdate(ProductCreate):
    pass


class ProductUpdatePartial(ProductCreate):
    name: Union[str, None] = None
    description: Union[str, None] = None
    price: Union[int, None] = None
    size: Union[int, None] = None


class Product(ProductBase):
    model_config = ConfigDict(from_attributes=True)

    id: int
