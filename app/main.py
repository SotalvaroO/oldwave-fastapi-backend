from fastapi import FastAPI
from starlette.responses import RedirectResponse
from app.src.routes.product_routes import route
from fastapi.middleware.cors import CORSMiddleware


app = FastAPI()
app.include_router(route,prefix='/api')

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get('/')
async def home():
    res = RedirectResponse(url='/docs')
    return res
