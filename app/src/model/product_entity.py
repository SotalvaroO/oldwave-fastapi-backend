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
    


class ProductDetailEntity(BaseModel):
    product_code: str
    name: str
    description: str
    brand: str
    city: str
    images: list
    reseller: str
    price: int
    rating: int