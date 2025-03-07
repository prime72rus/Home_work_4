from src.order import Order


def test_order(milky_product_1, capsys):
    order_1 = Order(milky_product_1, 3)
    assert order_1.name == "Сыр"
    assert order_1.quantity == 3
    assert order_1.total_amount == 615.0

    order_1.print_info()
    message = capsys.readouterr()
    assert message.out.strip() == "Товар: Сыр, количество: 3 шт., итоговая цена: 615.0 руб."