from src.order import Order


def test_order(milky_product_1, capsys):
    order_1 = Order(milky_product_1, 3)
    assert order_1.name == "Сыр"
    assert order_1.quantity == 3
    assert order_1.total_amount == 615.0

    order_1.print_info()
    message = capsys.readouterr()
    assert message.out.strip() == ("Продукт добавлен в заказ\n"
                                   "Обработка добавления продукта завершена\n"
                                   "Товар: Сыр, количество: 3 шт., итоговая цена: 615.0 руб.")


def test_order_zero_quantity(milky_product_zero_quantity, capsys):
    Order(milky_product_zero_quantity, 0)
    captured = capsys.readouterr()
    assert captured.out == ("Товар с нулевым или отрицательным количеством не может быть добавлен\n"
                            "Обработка добавления продукта завершена\n")