from typing import List
from app.src.repository import product_repository

def list_products_by_name_like(name: str):
    products: List = []
    products = product_repository.get_product_by_name_like(name)
    return products

    
def find_product_by_code(code:str):
    product_repository.update_product_search(code)
    product = product_repository.get_product_detail(code)
    return product
