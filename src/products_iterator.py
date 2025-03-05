from src.category import Category
from src.product import Product


class ProductsIterator:
    def __init__(self, category_obj):
        self.category = category_obj
        self.index = 0


    def __iter__(self):
        return self


    def __next__(self):
        if self.index < len(self.category.products_in_list):
            product_iter = self.category.products_in_list[self.index]
            self.index += 1
            return product_iter
        else:
            raise StopIteration
