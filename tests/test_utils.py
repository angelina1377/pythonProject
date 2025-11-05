import  json
import os
import pytest
from src.python_project import Product, Category


def load_json(relative_path: str) -> dict:
    # Получаем путь к корневому каталогу проекта
    project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
    full_path = os.path.join(project_root, "data", "products.json")

    try:
        with open(full_path, 'r', encoding='utf-8') as f:
            return json.load(f)
    except FileNotFoundError:
        print(f"Ошибка: файл не найден по пути {full_path}")
        raise


def create_objects_from_json(data):
    categories = []
    for category in data:
        name = category['name']
        description = category['description']
        products = []
        for product in category['products']:
            name_product = product["name"]
            description_product = product["description"]
            price_product = product["price"]
            quantity_product = product["quantity"]
            product_object = Product(name_product, description_product, price_product, quantity_product)
            products.append(product_object)
        category_object = Category(name, description, products)
        categories.append(category_object)
    return categories


def test_import_json_and_create_objects(tmp_path):
    try:
        data = load_json("products.json")

        # Проверяем структуру JSON
        assert isinstance(data, list)
        assert "name" in data[0]
        assert "description" in data[0]
        assert "products" in data[0]

        # Создаём объекты
        categories = create_objects_from_json(data)

        # Проверяем результат
        assert isinstance(categories, list)
        assert len(categories) > 0

        first_cat = categories[0]
        assert isinstance(first_cat, Category)
        assert hasattr(first_cat, "name")
        assert hasattr(first_cat, "description")
        assert isinstance(first_cat.products, list)

        if first_cat.products:
            first_prod = first_cat.products[0]
            assert isinstance(first_prod, Product)
            assert hasattr(first_prod, "name")
            assert hasattr(first_prod, "description")
            assert hasattr(first_prod, "price")
            assert hasattr(first_prod, "quantity")
    except FileNotFoundError as e:
        print(f"Ошибка: файл не найден по пути {e}")
        raise