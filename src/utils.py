import json
import os

from src.category import Category
from src.product import Product


def read_from_json(path: str) -> list[dict]:
    """
    Функция, которая принимает на вход путь до JSON-файла и возвращает список
    словарей с данными о продуктах. Если файл пустой,
    содержит не список или не найден, функция возвращает пустой список.
    """
    if not os.path.isfile(path) or os.path.getsize(path) == 0:
        return []
    try:
        with open(path, encoding="utf-8") as file_json:
            result = json.load(file_json)
        if not isinstance(result, list):
            return []
        else:
            return result
    except json.JSONDecodeError:
        return []


def create_object_from_dict(data: list[dict]) -> list[Category]:
    """
    Функция, которая принимает на вход список словарей, а возвращает список объектов класса Category
    """
    categories = []
    for category in data:
        products_list = []
        for product in category["products"]:
            products_list.append(Product(**product))
        category["products"] = products_list
        categories.append(Category(**category))
    return categories


if __name__ == "__main__":  # pragma: no cover
    data_from_json = read_from_json("../data/products.json")
    categories_list = create_object_from_dict(data_from_json)
    print(data_from_json)
    print(categories_list[0].products)
    print(Category.category_count)
    print(Category.product_count)
    for i in categories_list:
        print(f"Имя категории: {i.name}\nОписание: {i.description}")
