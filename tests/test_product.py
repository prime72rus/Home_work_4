def test_product_init(milky_product_1):
    assert milky_product_1.name == "Сыр"
    assert milky_product_1.description == "Молочный продукт"
    assert milky_product_1.price == 205.0
    assert milky_product_1.quantity == 10
