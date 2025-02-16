def test_category_init(bakery_category, milky_category):
    assert bakery_category.name == "Хлебобулочные изделия"
    assert bakery_category.description == "Хлеб и выпечка"
    assert len(bakery_category.products) == 2

    assert bakery_category.all_category_count == 2
    assert bakery_category.all_products_count == 4

    assert milky_category.all_category_count == 2
    assert milky_category.all_products_count == 4
