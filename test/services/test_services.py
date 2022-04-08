from app.src.service import product_service


def test_find_product_by_code_name_equals():
    assert product_service.find_product_by_code("1")["name"] == "iPhone 13 128 GB"


def test_find_product_by_code_price_equals():
    assert product_service.find_product_by_code("2")["price"] == 70000


def test_find_product_by_code_brand_equals():
    assert product_service.find_product_by_code("9")["brand"] == "Logitech"

def test_find_product_by_code_rating_equals():
    assert product_service.find_product_by_code("9")["rating"] == 5

def test_find_product_by_code_imgs_greater_than_zero_equals():
    assert len(product_service.find_product_by_code("9")["images"]) > 0


def test_list_products_by_name_like():
    assert len(product_service.list_products_by_name_like("")) == 12


def test_list_products_by_name_like_iphone():
    assert len(product_service.list_products_by_name_like("iphone")) == 2


def test_list_products_by_name_like_billetera():
    assert len(product_service.list_products_by_name_like("billetera")) == 1

