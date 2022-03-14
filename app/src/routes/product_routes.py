
from fastapi import APIRouter
from app.src.repository import product_repository

route = APIRouter(prefix='/product', tags=['Product'])

@route.get('')
async def get_products_by_name(name: str):
    response = await product_repository.get_product_by_name_like(name)
    return response