from unicodedata import name
from app.src.config.db_connection import product_collection
from app.src.model.product_entity import ProductEntity, ProductDetailEntity

# async def get_product_by_name_like(name: str):
#     products = []
#     cursor = product_collection.find({"name":{"$regex": name, "$options": "i"}})
#     async for document in cursor:
#         products.append(ProductEntity(**document))
#     return products

def get_product_by_name_like(name: str):
    products = []
    cursor = product_collection.find({"name":{"$regex": name, "$options": "i"}})
    for document in cursor:
        products.append(ProductEntity(**document))
    return products

def get_product_detail(code:str):
    document = product_collection.find_one({"product_code": code})
    return document