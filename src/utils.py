import json
import os
from python_project import Product, Category


def load_json(relative_path: str) -> dict:
    """Чтение JSON по относительному пути к проекту."""
    # Получаем путь к корневому каталогу проекта
    project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
    full_path = os.path.join(project_root, "data", "products.json")

    try:
        with open(full_path, 'r', encoding='utf-8') as f:  # Открываем файл в режиме чтения
            return json.load(f)  # Загружаем JSON-данные из файла
    except FileNotFoundError:
        print(f"Ошибка: файл не найден по пути {full_path}")
        raise


def create_objects_from_json(data):
    """
    Функция-помощник для создания объектов Product и Category из JSON-данных.
    """
    categories = []  # Список для хранения категорий

    # Проходим по каждой категории в данных
    for category in data:
        # Извлекаем данные категории
        name = category['name']
        description = category['description']
        products = []

        # Проходим по каждому продукту в категории
        for product in category['products']:
            # Извлекаем данные продукта
            name_product = product["name"]
            description_product = product["description"]
            price_product = product["price"]
            quantity_product = product["quantity"]

            # Создаем объект Product
            product_object = Product(name_product, description_product, price_product, quantity_product)
            products.append(product_object)  # Добавляем в список продуктов

        # Создаем объект Category
        category_object = Category(name, description, products)
        categories.append(category_object)  # Добавляем в список категорий

    return categories  # Возвращаем список созданных категорий
