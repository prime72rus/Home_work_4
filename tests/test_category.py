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
