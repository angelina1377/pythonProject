import pytest

from src.python_project import Product, Category, Smartphone, LawnGrass

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

#
def test_product_addition_same_type():
    p1 = Product("Чайник", "Металлический", 1500.0, 3)
    p2 = Product("Чайник", "Металлический", 1500.0, 7)
    result = p1 + p2

    assert result.name == "Чайник"
    assert result.quantity == 10
    assert result.price == 1500.0
    assert isinstance(result, Product)

def test_product_addition_different_types_raises_error():
    p = Product("Книга", "Фантастика", 499.0, 10)
    s = Smartphone("iPhone", "15 Pro", 100000.0, 2, "high", "15 Pro", "256GB", "Black")

    with pytest.raises(TypeError) as excinfo:
        p + s

    assert "Нельзя складывать товары разных типов" in str(excinfo.value)

def test_smartphone_creation():
    s = Smartphone("iPhone", "15 Pro", 100000.0, 2, "high", "15 Pro", "256GB", "Black")
    assert s.name == "iPhone"
    assert s.description == "15 Pro"
    assert s.price == 100000.0
    assert s.quantity == 2
    assert s.efficiency == "high"
    assert s.model == "15 Pro"
    assert s.memory == "256GB"
    assert s.color == "Black"



def test_smartphone_addition():
    s1 = Smartphone("iPhone", "15 Pro", 100000.0, 2, "high", "15 Pro", "256GB", "Black")
    s2 = Smartphone("iPhone", "15 Pro", 100000.0, 3, "high", "15 Pro", "256GB", "Black")
    result = s1 + s2

    assert result.name == "iPhone"
    assert result.quantity == 5
    assert result.model == "15 Pro"
    assert result.memory == "256GB"
    assert isinstance(result, Smartphone)

def test_lawngrass_creation():
    g = LawnGrass("Газон", "Зелёная трава", 500.0, 4, "Россия", "14 дней", "Зелёный")
    assert g.name == "Газон"
    assert g.description == "Зелёная трава"
    assert g.price == 500.0
    assert g.quantity == 4
    assert g.country == "Россия"
    assert g.germination_period == "14 дней"
    assert g.color == "Зелёный"



def test_lawngrass_addition():
    g1 = LawnGrass("Газон", "Зелёная трава", 500.0, 4, "Россия", "14 дней", "Зелёный")
    g2 = LawnGrass("Газон", "Зелёная трава", 500.0, 6, "Россия", "14 дней", "Зелёный")
    result = g1 + g2


    assert result.name == "Газон"
    assert result.quantity == 10
    assert result.country == "Россия"
    assert isinstance(result, LawnGrass)

def test_add_product_valid():
    category = Category("Электроника", "Смартфоны", [])
    phone = Smartphone("Pixel", "Android", 60000.0, 1, "mid", "7", "128GB", "White")

    category.add_product(phone)

    assert len(category.products) == 1
    assert category.products[0] == phone
    assert Category.product_count == 1



def test_add_non_product_raises_error():
    category = Category("Товары", "Разные", [])

    with pytest.raises(TypeError) as excinfo:
        category.add_product("Просто строка")

    assert "Можно добавлять только объекты класса Product" in str(excinfo.value)


    with pytest.raises(TypeError) as excinfo:
        category.add_product(123)

    assert "Можно добавлять только объекты класса Product" in str(excinfo.value)

    with pytest.raises(TypeError) as excinfo:
        category.add_product({"name": "Товар"})

    assert "Можно добавлять только объекты класса Product" in str(excinfo.value)


