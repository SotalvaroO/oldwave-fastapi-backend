from fastapi.testclient import TestClient
from unittest.mock import Mock
from app.main import app

mock = Mock()

client = TestClient(app)

def test_product_list_iphone():
    response = client.get("/api/product/?name=iphone")
    assert response.status_code == 200
    assert response.json()["items"][0]["city"] == "Medellin"

def test_product_detail():
    response = client.get("/api/product/1/detail")
    assert response.status_code == 200
    assert response.json()["product_code"] == "1"

def test_product_list_pagination_total():
    response = client.get("/api/product/?page=1&size=50")
    assert response.status_code == 200
    assert response.json()["total"] == 12

def test_product_list_pagination_small():
    response = client.get("/api/product/?page=1&size=5")
    assert response.status_code == 200
    assert response.json()["size"] == 5

def test_product_list_pagination_pages():
    response = client.get("/api/product/?page=3&size=3")
    assert response.status_code == 200
    assert response.json()["page"] == 3

def test_product_detail_reseller():
    response = client.get("/api/product/11/detail")
    assert response.status_code == 200
    assert response.json()["reseller"] == "Santiago Otálvaro"

def test_product_list_seller():
    response = client.get("/api/product/?page=1&size=50")
    assert response.status_code == 200
    assert response.json()["items"][10]["seller"] == "Ernesto Perez Frailejón Dev"