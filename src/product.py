from src.base_product import BaseProduct
from src.print_mixin import PrintMixin


class Product(BaseProduct, PrintMixin):
    name: str
    description: str
    price: float
    quantity: int

    def __init__(self, name: str, description: str, price: float, quantity: int):
        self.name = name
        self.description = description
        self.__price = price
        self.quantity = quantity
        super().__init__()

    def __str__(self):
        return f"{self.name}, {self.__price} руб. Остаток: {self.quantity} шт."

    def __add__(self, other):
        if type(other) is Product:
            return self.__price * self.quantity + other.__price * other.quantity
        else:
            raise TypeError("Входные данные не корректны")

    @classmethod
    def new_product(cls, new_product: dict, products_list: list = None):
        if list(new_product.keys()) == ["name", "description", "price", "quantity"]:
            name, description, price, quantity = new_product.values()
            if products_list:
                for product in products_list:
                    if product.name == name:
                        product.quantity += quantity
                        if product.price < price:
                            product.price = price
                        return product
            return cls(name, description, price, quantity)
        else:
            raise TypeError("Входные данные не корректны")

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, new_price: float):
        if new_price <= 0:
            print("Цена не должна быть нулевая или отрицательная")
        else:
            if new_price < self.__price:
                user_input = input(
                    'Подтвердите операцию снижения цены - "y" считается за согласие,'
                    "а любой другой ответ отменяет действие: "
                )
                if user_input == "y":
                    self.__price = float(new_price)
                else:
                    print("Отмена действия")
            else:
                self.__price = float(new_price)
