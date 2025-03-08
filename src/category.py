from src.base_product import BaseOrderCategory
from src.product import Product


class Category(BaseOrderCategory):
    name: str
    description: str
    products: list
    category_count = 0
    product_count = 0

    def __init__(self, name: str, description: str, products: list[Product]):
        self.name = name
        self.description = description
        self.__products = products if products else []
        Category.category_count += 1
        Category.product_count += len(products) if products else 0

    def __str__(self):
        sum_quantity = 0
        if len(self.__products) > 0:
            for product in self.__products:
                sum_quantity += product.quantity
        return f"{self.name}, количество продуктов: {sum_quantity} шт."

    def print_info(self):
        print(f"Категория: {self.name}, описание категории: {self.description}")

    def add_product(self, product: Product):
        if isinstance(product, Product):
            self.__products.append(product)
            Category.product_count += 1
        else:
            raise TypeError("Входные данные не корректны")

    @property
    def products(self):
        products_str = ""
        for product in self.__products:
            products_str += f"{str(product)}\n"
        return products_str

    @property
    def products_in_list(self):
        products_list = []
        for product in self.__products:
            products_list.append(product)
        return products_list
