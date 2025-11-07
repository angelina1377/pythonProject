import pytest

from src.python_project import Product, Category


def test_product_creation():
    # Создаем объект Product с конкретными параметрами
    p = Product("Телефон", "Смартфон с 128 ГБ", 29999.0, 5)

    # Проверяем, что все атрибуты объекта установлены правильно
    assert p.name == "Телефон"  # Проверяем название продукта
    assert p.description == "Смартфон с 128 ГБ"  # Проверяем описание
    assert p.price == 29999.0  # Проверяем цену
    assert p.quantity == 5  # Проверяем количество


def test_category_creation_with_products():
    # Создаем два продукта
    prod1 = Product("Книга", "Фантастика", 499.0, 10)
    prod2 = Product("Ручка", "Гелевая", 50.0, 100)

    # Создаем категорию с этими продуктами
    category = Category("Канцтовары", "Различные канцелярские товары", [prod1, prod2])

    # Проверяем атрибуты категории
    assert category.name == "Канцтовары"  # Проверяем название категории
    assert category.description == "Различные канцелярские товары"  # Проверяем описание
    assert isinstance(category.products, list)  # Проверяем, что products - список
    assert len(category.products) == 2  # Проверяем количество продуктов
    assert category.products[0].name == "Книга"  # Проверяем первый продукт
    assert category.products[1].name == "Ручка"  # Проверяем второй продукт


def test_category_counters():
    # Обнуляем счетчики категорий и продуктов перед тестом
    Category.category_count = 0
    Category.product_count = 0

    # Создаем продукт и категорию
    p1 = Product("Блокнот", "Альбом для заметок", 120.0, 20)
    c1 = Category("Канцтовары", "Описание", [p1])

    # Проверяем работу счетчиков
    assert Category.category_count == 1  # Должна быть создана 1 категория
    assert Category.product_count == len([p1])  # Должен быть учтен 1 продукт


def test_category_empty_products():
    # Обнуляем счетчики
    Category.category_count = 0
    Category.product_count = 0

    # Создаем категорию без продуктов
    empty_category = Category("Пустые товары", "Описание", [])

    # Проверяем корректность работы с пустой категорией
    assert empty_category.name == "Пустые товары"  # Проверяем название
    assert empty_category.products == []  # Проверяем пустой список продуктов
    assert Category.product_count == 0  # Проверяем счетчик продуктов
