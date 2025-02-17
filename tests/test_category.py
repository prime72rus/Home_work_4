def test_category_init(bakery_category, milky_category):
    assert bakery_category.name == "Хлебобулочные изделия"
    assert bakery_category.description == "Хлеб и выпечка"
    assert len(bakery_category.products) == 2

    assert bakery_category.category_count == 2
    assert bakery_category.product_count == 4

    assert milky_category.category_count == 2
    assert milky_category.product_count == 4
