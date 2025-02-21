import pytest

from src.product import Product
from src.category import Category


@pytest.fixture
def milky_product_1():
    return Product("Сыр", "Молочный продукт", 205.0, 10)


@pytest.fixture
def milky_product_2():
    return Product("Молоко", "Молочный продукт", 142.0, 12)


@pytest.fixture
def bakery_product_1():
    return Product("Батон французский", "Хлебобулочные изделия", 55.0, 5)


@pytest.fixture
def bakery_product_2():
    return Product("Хлеб ржаной", "Хлебобулочные изделия", 61.0, 7)


@pytest.fixture
def milky_category(milky_product_1, milky_product_2):
    return Category("Молочные продукты", "Молоко и его производные", [milky_product_1, milky_product_2])


@pytest.fixture
def bakery_category(bakery_product_1, bakery_product_2):
    return Category("Хлебобулочные изделия", "Хлеб и выпечка", [bakery_product_1, bakery_product_2])


@pytest.fixture
def data_from_json():
    return [
        {
            "name": "Смартфоны",
            "description":
            "Смартфоны, как средство не только коммуникации, но и получение дополнительных функций для удобства жизни",
            "products": [{
                "name": "Samsung Galaxy C23 Ultra",
                "description": "256GB, Серый цвет, 200MP камера",
                "price": 180000.0,
                "quantity": 5
              }]
        }
    ]
