from fastapi.testclient import TestClient
from app.main import app



client = TestClient(app)

def test_product_list():
    response = client.get("/api/product/?name=iphone")
    assert response.status_code == 200
    assert response.json()["items"][0]["city"] == "Medellin"

def test_product_detail():
    response = client.get("/api/product/1/detail")
    assert response.status_code == 200
    assert response.json() == {
        "product_code": "1",
        "name": "Iphone 13 promax hd 4k 420",
        "description": "Celular caro",
        "brand": "adidas",
        "city": "Medellin",
        "images": [
            "f",
            "a"
        ],
        "reseller": "presi",
        "price": 70000,
        "rating": 5
    }