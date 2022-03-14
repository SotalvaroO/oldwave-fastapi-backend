from unicodedata import name
from app.src.config.db_connection import product_collection
from app.src.model.product_entity import ProductEntity, ProductDetailEntity

async def get_product_by_name_like(name: str):
    document = await product_collection.find({"name": '/{name}/'})
    return document

async def get_product_detail(code:str):
    document = await product_collection.find_one({"product_code": code})
    return document