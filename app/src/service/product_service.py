from http.client import HTTPException
from typing import List
from app.src.repository import product_repository

async def list_products_by_name_like(name: str):
    products: List = []
    products = await product_repository.get_product_by_name_like(name)
    return products

    
async def find_product_by_code(code:str):

    product = await product_repository.get_product_detail(code)
    return product
