class Product:
    name: str
    description: str
    price: float
    quantity: int

    def __init__(self, name: str, description: str, price: float, quantity: int):
        self.name = name
        self.description = description
        self.price = price
        self.quantity = quantity

    @classmethod
    def new_product(cls, new_product: dict, products_list: list=None):
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
            raise ValueError("Входные данные не корректны")
