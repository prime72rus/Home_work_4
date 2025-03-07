from src.base_product import BaseOrderCategory
from src.product import Product


class Order(BaseOrderCategory):
    name: str
    quantity: int
    total_amount: float

    def __init__(self, product: Product, quantity: int) -> None:
        self.name = product.name
        self.quantity = quantity
        self.total_amount = product.price * quantity

    def print_info(self):
        print(f"Товар: {self.name}, количество: {self.quantity} шт., итоговая цена: {self.total_amount} руб.")
