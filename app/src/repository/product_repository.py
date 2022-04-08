from app.src.config.db_connection import product_collection
from app.src.model.product_entity import ProductEntity


# async def get_product_by_name_like(name: str):
#     products = []
#     cursor = product_collection.find({"name":{"$regex": name, "$options": "i"}})
#     async for document in cursor:
#         products.append(ProductEntity(**document))
#     return products

def get_product_by_name_like(name: str):
    products = []
    cursor = product_collection.find({"name":{"$regex": name, "$options": "i"}}).sort('search_quantity', -1)
    for document in cursor:
        products.append(ProductEntity(**document))
    return products

def get_product_detail(code:str):
    document = product_collection.find_one({"product_code": code})
    return document

def update_product_search(code:str):
    document = product_collection.find_one({"product_code": code})
    search_quantity = int(document.get('search_quantity')) + 1
    product_collection.update_one(
        {"product_code": code},
        {"$set": {"search_quantity": search_quantity}}
    )
        