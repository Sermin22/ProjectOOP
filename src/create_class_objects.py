import os
import json
from src.product_and_category import Product, Category


def read_json(path: str) -> list[dict]:
    """Функция, которая читает json-файл"""

    full_path = os.path.abspath(path)
    with open(full_path, "r", encoding="UTF-8") as file:
        data = json.load(file)
    return data


def create_objects_from_json(data):
    """Функция, которая будет из json-файл создает объекты классов"""

    categories = []
    for key_data in data:
        products = []
        for key_products in key_data["products"]:
            products.append(Product(**key_products))
        key_data["products"] = products
        categories.append(Category(**key_data))

    return categories


# if __name__ == "__main__":
#     raw_data = read_json("../data/products.json")
#     print(raw_data)
#     class_data = create_objects_from_json(raw_data)
#     print(class_data[0].name)
#     print(class_data[0].products)
