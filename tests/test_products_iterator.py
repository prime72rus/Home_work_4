import pytest


def test_products_iterator(products_iterator):
    iter(products_iterator)
    assert products_iterator.index == 0
    assert next(products_iterator).name == "Сыр"
    assert next(products_iterator).description == "Молочный продукт"

    with pytest.raises(StopIteration):
        next(products_iterator)
