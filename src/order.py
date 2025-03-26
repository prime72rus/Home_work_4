from src.base_product import BaseOrderCategory
from src.product import Product
from src.exceptions import ZeroProductQuantity


class Order(BaseOrderCategory):
    name: str
    quantity: int
    total_amount: float

    def __init__(self, product: Product, quantity: int) -> None:
        try:
            if product.quantity <= 0 or quantity <= 0:
                raise ZeroProductQuantity("Товар с нулевым или отрицательным количеством не может быть добавлен")
        except ZeroProductQuantity as e:
            print(str(e))
        else:
            self.name = product.name
            self.quantity = quantity
            self.total_amount = product.price * quantity
            print("Продукт добавлен в заказ")
        finally:
            print("Обработка добавления продукта завершена")


    def print_info(self):
        print(f"Товар: {self.name}, количество: {self.quantity} шт., итоговая цена: {self.total_amount} руб.")
