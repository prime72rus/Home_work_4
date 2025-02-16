from src.product import Product


class Category:
    name: str
    description: str
    products: list
    all_category_count = 0
    all_products_count = 0

    def __init__(self, name, description, products=None):
        self.name = name
        self.description = description
        self.products = products
        Category.all_category_count += 1
        Category.all_products_count += len(products) if products else 0


if __name__ == "__main__":   # pragma: no cover

    pr1 = Product("Сыр", "Молочный продукт", 205.0, 10)
    pr2 = Product("Молоко", "Молочный продукт", 142.0, 12)
    pr3 = Product("Творог", "Молочный продукт", 95.0, 6)

    product_list = [pr1, pr2, pr3]

    cat1 = Category("Молочные продукты", "Молоко и его производные", product_list)

    print(cat1.name)
    print(cat1.description)
    for i in cat1.products:
        print(i.name, end=" ")
    print("\n")
    print(Category.all_category_count)
    print(Category.all_products_count)
