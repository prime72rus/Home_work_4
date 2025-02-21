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


if __name__ == "__main__":  # pragma: no cover
    pr1 = Product("Сыр", "Молочный продукт", 205.0, 10)

    print(pr1.name)
    print(pr1.description)
    print(pr1.price)
    print(pr1.quantity)
