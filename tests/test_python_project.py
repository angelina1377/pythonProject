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

def test_product_str():
    """
    Тест метода __str__ класса Product.
    Цель: проверить, что строковое представление соответствует заданному формату.
    Ожидаемый формат: "Название продукта:{name}, {price} руб. Остаток: {quantity} шт."
    """
    p = Product("Чай", "Чёрный", 150.0, 10)
    expected = "Название продукта:Чай, 150.0 руб. Остаток: 10 шт."
    assert str(p) == expected


def test_product_add_valid():
    """
    Тест корректного сложения двух объектов Product через оператор +.
    Цель: проверить расчёт общей стоимости товаров на складе.
    Формула: (price₁ × quantity₁) + (price₂ × quantity₂)
    """
    a = Product("Яблоко", "Свежее", 100.0, 10)
    b = Product("Банан", "Спелый", 200.0, 2)
    total = a + b

    # Проверка результата по формуле: 100×10 + 200×2 = 1000 + 400 = 1400
    assert total == 1400
    # Проверка типа возвращаемого значения
    assert isinstance(total, (int, float))

def test_product_add_invalid_type():
    """
    Тест обработки некорректного типа при сложении.
    Цель: убедиться, что при попытке сложить Product с не-Product возникает TypeError.
    Проверяется:
    - возникновение исключения
    - корректность текста ошибки
    """
    a = Product("Яблоко", "Свежее", 100.0, 10)
    with pytest.raises(TypeError) as excinfo:
        a + "не продукт"
    assert "Можно складывать только объекты класса Product" in str(excinfo.value)

def test_product_add_with_none():
    """
    Тест сложения Product с None.
    Цель: проверить обработку граничного случая (None).
    Ожидаемое поведение: выброс TypeError с корректным сообщением.
    """
    a = Product("Яблоко", "Свежее", 100.0, 10)
    with pytest.raises(TypeError) as excinfo:
        a + None
    assert "Можно складывать только объекты класса Product" in str(excinfo.value)

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
    """
    Тест работы счётчиков категорий и продуктов.
    Цель: проверить увеличение счётчиков при создании новой категории.
    Проверяемые атрибуты:
    - Category.category_count (количество созданных категорий)
    - Category.product_count (количество продуктов в категории)
    """
    # Обнуление счётчиков перед тестом
    Category.category_count = 0
    Category.product_count = 0

    p1 = Product("Блокнот", "Альбом для заметок", 120.0, 20)
    c1 = Category("Канцтовары", "Описание", [p1])


    assert Category.category_count == 1  # Должна быть создана 1 категория
    assert Category.product_count == 1  # В категории 1 продукт

def test_category_empty_products():
    """
    Тест создания категории без продуктов.
    Цель: проверить работу с пустым списком продуктов.
    """
    # Обнуление счётчиков
    Category.category_count = 0
    Category.product_count = 0

    empty_category = Category("Пустые товары", "Описание", [])

    assert empty_category.name == "Пустые товары"  # Проверка имени
    assert empty_category.products == []  # Проверка пустого списка
    assert Category.product_count == 0  # В пустой категории 0 продуктов

def test_category_str_with_products():
    """
    Тест строкового представления категории с несколькими продуктами.
    Цель: проверить корректный подсчёт общего количества товаров.
    Ожидаемый формат: "Название категории:{name}, количество продуктов: {total} шт."
    """
    prod1 = Product("Футболка", "Хлопок", 500.0, 3)
    prod2 = Product("Шорты", "Лён", 800.0, 2)
    category = Category("Одежда", "Летняя коллекция", [prod1, prod2])

    expected = "Название категории:Одежда, количество продуктов: 5 шт."  # 3 + 2 = 5
    assert str(category) == expected



def test_category_str_empty():
    """
    Тест строкового представления пустой категории.
    Цель: проверить вывод для категории без продуктов.
    Ожидаемый результат: количество продуктов = 0.
    """
    empty_category = Category("Пустая категория", "Нет товаров", [])
    expected = "Название категории:Пустая категория, количество продуктов: 0 шт."
    assert str(empty_category) == expected



def test_category_str_single_product():
    """
    Тест строкового представления категории с одним продуктом.
    Цель: проверить подсчёт для крайнего случая (1 продукт).
    """
    prod = Product("Кружка", "Керамическая", 300.0, 7)
    category = Category("Посуда", "Для кухни", [prod])

    expected = "Название категории:Посуда, количество продуктов: 7 шт."
    assert str(category) == expected



def test_category_products_list_mutation():
    """
    Тест динамического пересчёта количества при изменении списка продуктов.
    Цель: убедиться, что __str__ отражает актуальные изменения в products.
    Сценарий:
    1. Создаём категорию с одним продуктом (quantity=4)
    2. Добавляем второй продукт (quantity=15)
    3. Проверяем, что str() возвращает обновлённую сумму (19)
    """
    prod = Product("Лампа", "Светодиодная", 600.0, 4)
    category = Category("Освещение", "Светильники", [prod])

    # Добавляем новый продукт в список
    new_prod = Product("Свеча", "Восковая", 100.0, 15)
    category.products.append(new_prod)

    # Проверяем обновлённое строковое представление
    result = str(category)
    expected = "Название категории:Освещение, количество продуктов: 19 шт."  # 4 + 15 = 19
    assert result == expected

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
