from fastapi import FastAPI
from starlette.responses import RedirectResponse
from app.src.routes.product_routes import route

app = FastAPI()
app.include_router(route,prefix='/api')

@app.get('/')
async def home():
    res = RedirectResponse(url='/docs')
    print(res)
    return res
