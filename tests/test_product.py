import pytest

from src.product import Product
from tests.conftest import add_new_product


def test_product_init(milky_product_1):
    assert milky_product_1.name == "Сыр"
    assert milky_product_1.description == "Молочный продукт"
    assert milky_product_1.price == 205.0
    assert milky_product_1.quantity == 10


def test_new_product_1(add_new_product):
    new_product_1 = Product.new_product(add_new_product)
    assert new_product_1.name == "Samsung Galaxy S23 Ultra"
    assert new_product_1.description == "256GB, Серый цвет, 200MP камера"
    assert new_product_1.price == 180000.0
    assert new_product_1.quantity == 5


def test_new_product_2(add_new_product, product_list):
    new_product_2 = Product.new_product(add_new_product, product_list)
    assert new_product_2.quantity == 10


def test_new_product_3(add_new_product_error):
    with pytest.raises(ValueError, match="Входные данные не корректны"):
        Product.new_product(add_new_product_error)


def test_new_product_4(add_new_product_price, product_list):
    new_product_4 = Product.new_product(add_new_product_price, product_list)
    assert new_product_4.price == 200000.0


def test_price_1(capsys, product_1):
    product_1.price = -100
    captured = capsys.readouterr()
    assert captured.out == "Цена не должна быть нулевая или отрицательная\n"


def test_price_2(capsys, product_1):
    product_1.price = 0
    captured = capsys.readouterr()
    assert captured.out == "Цена не должна быть нулевая или отрицательная\n"


def test_price_confirm(monkeypatch, product_1):
    monkeypatch.setattr("builtins.input", lambda _: "y")
    product_1.price = 100.0
    assert product_1.price == 100.0


def test_price_no_confirm(monkeypatch, capsys, product_1):
    monkeypatch.setattr("builtins.input", lambda _: "n")
    product_1.price = 80.0
    assert product_1.price == 210000.0
    captured = capsys.readouterr()
    assert captured.out == "Отмена действия\n"


def test_price_3(product_1):
    product_1.price = 220000.0
    assert product_1.price == 220000.0


def test_product_method_add(milky_product_1, milky_product_2):
    assert milky_product_1 + milky_product_2 == 3754.0


def test_product_method_add_error(milky_product_1, error_class_product_1):
    with pytest.raises(TypeError, match="Входные данные не корректны"):
        result = milky_product_1 + error_class_product_1
