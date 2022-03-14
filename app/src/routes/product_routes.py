
from fastapi import APIRouter, HTTPException
from app.src.repository import product_repository
from app.src.model.product_entity import ProductEntity, ProductDetailEntity

route = APIRouter(prefix='/product', tags=['Product'])

@route.get('')
async def get_products_by_name(name: str):
    response = await product_repository.get_product_by_name_like(name)
    return response

@route.get('/detail/{code}', response_model=ProductDetailEntity)
async def get_product_detail_by_code(code : str):
    response = await product_repository.get_product_detail(code)
    if response:
        return response
    raise HTTPException(404, "No se encontró el producto con el código {code}")