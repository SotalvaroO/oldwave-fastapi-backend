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
        "name": "iPhone 13 128 GB",
        "description": "Celular Iphone muy costoso",
        "brand": "Apple",
        "city": "Medellin",
        "images": [
            "https://firebasestorage.googleapis.com/v0/b/oldwave-fastapi-backend.appspot.com/o/product_pictures%2Fimage_2022-03-19_000724.png?alt=media&token=8f04bae0-d3f3-48b9-8ddf-35fa8b872a80",
            "https://firebasestorage.googleapis.com/v0/b/oldwave-fastapi-backend.appspot.com/o/product_pictures%2Fimage_2022-03-19_000739.png?alt=media&token=c558752d-7de0-4e6b-b069-b6c85f752a35",
            "https://firebasestorage.googleapis.com/v0/b/oldwave-fastapi-backend.appspot.com/o/product_pictures%2Fimage_2022-03-19_000756.png?alt=media&token=faad12c4-1e89-4098-a908-d4e032e4feda",
            "https://firebasestorage.googleapis.com/v0/b/oldwave-fastapi-backend.appspot.com/o/product_pictures%2Fimage_2022-03-19_000814.png?alt=media&token=3df0febd-da32-47cc-a022-3bdf8930c68a"
        ],
        "reseller": "Juan Esteban Ospina",
        "price": 70000,
        "rating": 5
    }