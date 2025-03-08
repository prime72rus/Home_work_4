import pytest


def test_category_init(bakery_category, milky_category):
    assert bakery_category.name == "Хлебобулочные изделия"
    assert bakery_category.description == "Хлеб и выпечка"
    assert (
        bakery_category.products
        == "Батон французский, 55.0 руб. Остаток: 5 шт.\nХлеб ржаной, 61.0 руб. Остаток: 7 шт.\n"
    )

    assert bakery_category.category_count == 2
    assert bakery_category.product_count == 4

    assert milky_category.category_count == 2
    assert milky_category.product_count == 4


def test_add_product(milky_category, milky_product_2):
    milky_category.add_product(milky_product_2)
    assert milky_category.category_count == 3


def test_add_product_error(milky_category, add_new_product):
    with pytest.raises(TypeError, match="Входные данные не корректны"):
        milky_category.add_product(add_new_product)


def test_category_method_str(milky_category):
    assert str(milky_category) == "Молочные продукты, количество продуктов: 22 шт."


def test_category_method_products_in_list(milky_category):
    assert milky_category.products_in_list[0].name == "Сыр"

def test_print_info(capsys, milky_category):
    milky_category.print_info()
    message = capsys.readouterr()
    assert (message.out.strip().split("\n")[-1] ==
            "Категория: Молочные продукты, описание категории: Молоко и его производные")