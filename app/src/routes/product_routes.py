
from fastapi import APIRouter, HTTPException, status
from app.src.service import product_service
from app.src.model.product_entity import ProductDetailEntity

route = APIRouter(prefix='/product', tags=['Product'])

@route.get('')
async def get_products_by_name(name: str):
    products = await product_service.list_products_by_name_like(name)
    if products:
        return products
    raise HTTPException(status_code=status.HTTP_204_NO_CONTENT)

@route.get('/{code}/detail/', response_model=ProductDetailEntity)
async def get_product_detail_by_code(code : str):
    response = await product_service.find_product_by_code(code)
    if response:
        return response
    raise HTTPException(status_code=404, detail =f"No existe el producto con código {code}")