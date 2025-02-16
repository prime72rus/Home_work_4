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
