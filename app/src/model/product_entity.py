from typing import List
from pydantic import BaseModel


class ProductEntity(BaseModel):
    product_code: str
    name: str
    brand: str
    thumbnail: str
    city: str
    price: int
    seller: str   
    rating: int
    search_quantity: int
    


class ProductDetailEntity(BaseModel):
    product_code: str
    name: str
    description: str
    brand: str
    city: str
    images: List[str]
    reseller: str
    price: int
    rating: int