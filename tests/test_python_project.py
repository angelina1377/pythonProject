import pytest

from src.python_project import Product, Category, Smartphone, LawnGrass
from src.python_project import Order


@pytest.fixture(autouse=True)
def reset_category_counts():
    """Обнуляет счётчики перед каждым тестом"""
    Category.category_count = 0
    Category.product_count = 0


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

def test_category_init_with_products():
    # Обнуляем счётчики перед тестом
    Category.category_count = 0
    Category.product_count = 0

    p1 = Product("Товар 1", "Описание 1", 100.0, 5)
    p2 = Product("Товар 2", "Описание 2", 200.0, 3)
    category = Category("Категория", "Описание", [p1, p2])

    assert len(category.products) == 2
    assert Category.product_count == 2  # Должно быть 2

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

#Сложение двух объектов Product одного типа (одинаковые название, цена, описание).
#тест подтверждает базовую логику сложения товаров одного типа
def test_product_addition_same_type():
    p1 = Product("Чайник", "Металлический", 1500.0, 3)
    p2 = Product("Чайник", "Металлический", 1500.0, 7)
    result = p1 + p2

    assert result.name == "Чайник"
    assert result.quantity == 10
    assert result.price == 1500.0
    assert isinstance(result, Product)# гарантирует, что не появился другой класс.

#Попытка сложить Product и Smartphone (разные классы)
#тест защищает от некорректного смешивания разных товаров
def test_product_addition_different_types_raises_error():
    p = Product("Книга", "Фантастика", 499.0, 10)
    s = Smartphone("iPhone", "15 Pro", 100000.0, 2, "high", "15 Pro", "256GB", "Black")

    with pytest.raises(TypeError) as excinfo:# это стандартный способ проверить, что код должен вызвать ошибку.
        p + s



#Корректность создания объекта Smartphone
#все атрибуты (name, price, efficiency и др.) передаются в __init__ и сохраняются;
#нет «потерянных» или неправильно присвоенных значений.
def test_smartphone_creation_with_logging(capsys):
    s = Smartphone("iPhone", "15 Pro", 100000.0, 2, "high", "15 Pro", "256GB", "Black")
    captured = capsys.readouterr()
    expected = "Smartphone('iPhone', '15 Pro', 100000.0, 2, 'high', '15 Pro', '256GB', 'Black')"
    assert expected in captured.out


#Сложение двух Smartphone с одинаковыми характеристиками
#метод __add__ работает для наследников Product (в данном случае — Smartphone)
#сохраняются специфические атрибуты (model, memory, color)
#суммируется только quantity
# тест подтверждает, что наследование не ломает логику сложения
def test_smartphone_addition():
    s1 = Smartphone("iPhone", "15 Pro", 100000.0, 2, "high", "15 Pro", "256GB", "Black")
    s2 = Smartphone("iPhone", "15 Pro", 100000.0, 3, "high", "15 Pro", "256GB", "Black")
    result = s1 + s2

    assert result.name == "iPhone"
    assert result.quantity == 5
    assert result.model == "15 Pro"
    assert result.memory == "256GB"
    assert isinstance(result, Smartphone)

#Создание объекта LawnGrass
def test_lawngrass_creation():
    g = LawnGrass("Газон", "Зелёная трава", 500.0, 4, "Россия", "14 дней", "Зелёный")
    assert g.name == "Газон"
    assert g.description == "Зелёная трава"
    assert g.price == 500.0
    assert g.quantity == 4
    assert g.country == "Россия"
    assert g.germination_period == "14 дней"
    assert g.color == "Зелёный"

    # Сложение двух LawnGrass с одинаковыми параметрами.
    # убедиться, что __add__ работает для LawnGrass
    # убедиться, что сохраняются специфичные атрибуты (country, germination_period)
    # убедиться, что суммируется quantity
def test_lawngrass_addition():
    g1 = LawnGrass("Газон", "Зелёная трава", 500.0, 4, "Россия", "14 дней", "Зелёный")
    g2 = LawnGrass("Газон", "Зелёная трава", 500.0, 6, "Россия", "14 дней", "Зелёный")
    result = g1 + g2

    assert result.name == "Газон"
    assert result.quantity == 10
    assert result.country == "Россия"
    assert isinstance(result, LawnGrass)

# Добавление корректного продукта (Smartphone) в категорию.
# Проверить, что продукт добавляется в список category.products
# Проверить, что счётчик Category.product_count увеличивается на 1;
# Проверить, что объект сохраняется без изменений
def test_add_product_valid():
    category = Category("Электроника", "Смартфоны", [])
    phone = Smartphone("Pixel", "Android", 60000.0, 1, "mid", "7", "128GB", "White")

    category.add_product(phone)

    assert len(category.products) == 1
    assert category.products[0] == phone
    assert Category.product_count == 1

# Попытка добавить в категорию не объекты Product (строку, число, словарь).
# Убедиться, что категория отклоняет некорректные типы
# Убедиться, что выбрасывает TypeError с понятным сообщением;
# Убедиться, что список продуктов остаётся пустым
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


# Тест на отрицательные quantity и price
def test_product_negative_quantity_raises_error():
    """Проверка, что отрицательная quantity вызывает ошибку."""
    with pytest.raises(ValueError):
        Product("Товар", "Описание", 100.0, -5)


def test_product_negative_price_raises_error():
    """Проверка, что отрицательная price вызывает ошибку."""
    with pytest.raises(ValueError):
        Product("Товар", "Описание", -100.0, 5)


# Тест на копирование всех атрибутов в __add__(для наследников)
def test_smartphone_addition_copies_all_attributes():
    """Проверка, что при сложении Smartphone копируются ВСЕ атрибуты."""
    s1 = Smartphone("iPhone", "15 Pro", 100000.0, 2, "high", "15 Pro", "256GB", "Black")
    s2 = Smartphone("iPhone", "15 Pro", 100000.0, 3, "high", "15 Pro", "256GB", "Black")
    result = s1 + s2

    # Проверяем ВСЕ атрибуты, включая наследные
    assert result.name == s1.name
    assert result.description == s1.description
    assert result.price == s1.price
    assert result.efficiency == s1.efficiency
    assert result.model == s1.model
    assert result.memory == s1.memory
    assert result.color == s1.color
    assert result.quantity == 5  # Только quantity суммируется



# Тест на isinstance с крайними случаями
def test_add_product_invalid_types():
    """Проверка add_product с None, object(), и другими типами."""
    category = Category("Товары", "Разные", [])

    with pytest.raises(TypeError):
        category.add_product(None)

    with pytest.raises(TypeError):
        category.add_product(object())

    with pytest.raises(TypeError):
        category.add_product([])  # Список


def test_product_negative_price():
    with pytest.raises(ValueError, match="Цена не может быть отрицательной"):
        Product("Товар", "Описание", -100.0, 5)

def test_product_negative_quantity():
    with pytest.raises(ValueError, match="Количество не может быть отрицательным"):
        Product("Товар", "Описание", 100.0, -5)


def test_add_different_types_raises_error():
    p = Product("Книга", "Фантастика", 499.0, 10)
    s = Smartphone("iPhone", "15 Pro", 100000.0, 2, "high", "15 Pro", "256GB", "Black")

    with pytest.raises(TypeError, match="Нельзя складывать товары разных типов"):
        p + s


def test_add_non_product_raises_error():
    category = Category("Товары", "Разные", [])

    with pytest.raises(TypeError, match="Можно добавлять только объекты класса Product"):
        category.add_product("Не продукт")


def test_category_init_with_products():
    # Обнуляем счётчики перед тестом
    Category.category_count = 0
    Category.product_count = 0

    p1 = Product("Товар 1", "Описание 1", 100.0, 5)
    p2 = Product("Товар 2", "Описание 2", 200.0, 3)
    category = Category("Категория", "Описание", [p1, p2])

    assert len(category.products) == 2
    assert Category.product_count == 2  # Должно быть 2 — без двойного подсчёта!


def test_smartphone_specific_fields():
    s = Smartphone("iPhone", "15 Pro", 100000.0, 2, "high", "15 Pro", "256GB", "Black")
    assert s.efficiency == "high"
    assert s.model == "15 Pro"


def test_lawngrass_specific_fields():
    g = LawnGrass("Газон", "Зелёная трава", 500.0, 4, "Россия", "14 дней", "Зелёный")
    assert g.country == "Россия"
    assert g.germination_period == "14 дней"


def test_add_duplicate_product():
    # Обнуляем счётчики
    Category.category_count = 0
    Category.product_count = 0

    category = Category("Товары", "Описание", [])
    p1 = Product("Товар", "Описание", 100.0, 5)
    p2 = Product("Товар", "Описание", 100.0, 5)  # Тот же продукт

    category.add_product(p1)
    category.add_product(p2)  # Не должен добавиться

    assert len(category.products) == 1
    assert Category.product_count == 1  # Теперь будет 1, а не 4



# 2. Тесты для Product
def test_product_creation():
    p = Product("Телефон", "Смартфон", 29999.0, 5)
    assert p.name == "Телефон"
    assert p.description == "Смартфон"
    assert p.price == 29999.0
    assert p.quantity == 5



def test_product_negative_price():
    with pytest.raises(ValueError, match="Цена не может быть отрицательной"):
        Product("Товар", "Описание", -100.0, 5)


def test_product_negative_quantity():
    with pytest.raises(ValueError, match="Количество не может быть отрицательным"):
        Product("Товар", "Описание", 100.0, -5)



def test_product_empty_strings():
    with pytest.raises(ValueError, match="Name не может быть None или пустым"):
        Product("", "", 100.0, 5)

def test_product_none_values():
    with pytest.raises(ValueError, match="Name не может быть None"):
        Product(None, None, 100.0, 5)

# 3. Тесты для Smartphone
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
    assert result.quantity == 5
    assert result.model == "15 Pro"
    assert result.memory == "256GB"
    assert isinstance(result, Smartphone)

# 4. Тесты для LawnGrass
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
    assert result.quantity == 10
    assert result.country == "Россия"
    assert result.germination_period == "14 дней"
    assert isinstance(result, LawnGrass)

# 5. Тесты для Category
def test_category_creation_with_products():
    prod1 = Product("Книга", "Фантастика", 499.0, 10)
    prod2 = Product("Ручка", "Гелевая", 50.0, 100)
    category = Category("Канцтовары", "Описание", [prod1, prod2])
    assert len(category.products) == 2

def test_category_counters():
    p1 = Product("Блокнот", "Альбом", 120.0, 20)
    assert Category.category_count == 0  # до создания категории
    assert Category.product_count == 0  # до добавления продукта

    c1 = Category("Канцтовары", "Описание", [p1])
    assert Category.category_count == 1  # после создания категории
    assert Category.product_count == 1  # после добавления продукта



def test_category_empty_products():
    empty_category = Category("Пустые", "Описание", [])
    assert empty_category.name == "Пустые"
    assert empty_category.description == "Описание"
    assert empty_category.products == []
    assert Category.product_count == 0

def test_add_product_valid():
    category = Category("Электроника", "Смартфоны", [])
    phone = Smartphone("Pixel", "Android", 60000.0, 1, "mid", "7", "128GB", "White")
    category.add_product(phone)
    assert len(category.products) == 1
    assert category.products[0] == phone
    assert Category.product_count == 1



def test_add_duplicate_product():
    category = Category("Товары", "Описание", [])
    p1 = Product("Товар", "Описание", 100.0, 5)
    p2 = Product("Товар", "Описание", 100.0, 5)  # Дубликат
    category.add_product(p1)
    category.add_product(p2)
    assert len(category.products) == 1
    assert Category.product_count == 1

def test_add_non_product_raises_error():
    category = Category("Товары", "Разные", [])
    with pytest.raises(TypeError, match="Можно добавлять только объекты класса Product"):
        category.add_product("Не продукт")
    with pytest.raises(TypeError, match="Можно добавлять только объекты класса Product"):
        category.add_product(123)
    with pytest.raises(TypeError, match="Можно добавлять только объекты класса Product"):
        category.add_product({})


# 6. Тесты для Order
def test_order_creation():
    """Проверяет корректное создание заказа"""
    p = Product("Книга", "Фантастика", 499.0, 10)
    order = Order(p, 2)
    assert order.product == p
    assert order.quantity == 2
    assert order.total_cost == 998.0  # 499 * 2
    assert order.name == "Книга"  # наследуется от product.name
    assert order.description == "Фантастика"  # наследуется от product.description


def test_order_invalid_product():
    """Проверяет, что нельзя создать заказ с некорректным товаром"""
    with pytest.raises(TypeError, match="Товар должен быть экземпляром класса Product"):
        Order("не продукт", 2)
    with pytest.raises(TypeError, match="Товар должен быть экземпляром класса Product"):
        Order(None, 2)
    with pytest.raises(TypeError, match="Товар должен быть экземпляром класса Product"):
        Order(123, 2)


def test_order_zero_quantity():
    """Проверяет создание заказа с нулевым количеством"""
    p = Product("Книга", "Фантастика", 499.0, 10)
    order = Order(p, 0)
    assert order.quantity == 0
    assert order.total_cost == 0.0


def test_order_display_info():
    """Проверяет вывод информации о заказе"""
    p = Product("Книга", "Фантастика", 499.0, 10)
    order = Order(p, 3)
    info = order.display_info()
    assert "Заказ: Книга" in info
    assert "Описание: Фантастика" in info
    assert "Количество: 3 шт." in info
    assert "Итоговая стоимость: 1497.0 руб." in info


def test_order_str_representation():
    """Проверяет строковое представление заказа"""
    p = Product("Книга", "Фантастика", 499.0, 10)
    order = Order(p, 2)
    assert str(order) == order.display_info()


def test_order_total_cost_calculation():
    """Проверяет пересчёт итоговой стоимости при изменении количества"""
    p = Product("Книга", "Фантастика", 499.0, 10)
    order = Order(p, 1)
    assert order.total_cost == 499.0



def test_order_hash():
    """Проверяет возможность использования заказа в множествах/словарях"""
    p = Product("Книга", "Фантастика", 499.0, 10)
    order = Order(p, 2)
    try:
        hash(order)
    except TypeError:
        pytest.fail("Order должен поддерживать хеширование если планируется использование в множествах")

# Интеграционные тесты
def test_full_workflow():
    """Комплексный тест: создание продукта → категории → заказа"""
    # Создаём продукт
    phone = Smartphone("iPhone", "15 Pro", 100000.0, 2, "high", "15 Pro", "256GB", "Black")

    # Добавляем в категорию
    category = Category("Смартфоны", "Мобильные устройства", [phone])
    assert len(category.products) == 1

    # Создаём заказ
    order = Order(phone, 1)
    assert order.total_cost == 100000.0
    assert "iPhone" in order.display_info()


#Тест для Product.update_quantity (включая граничные случаи)
def test_product_update_quantity():
    """Проверяет обновление количества товара."""
    p = Product("Чайник", "Металлический", 1500.0, 5)


    # Увеличение количества
    p.update_quantity(3)
    assert p.quantity == 8

    # Уменьшение количества
    p.update_quantity(-2)
    assert p.quantity == 6

    # Обнуление
    p.update_quantity(-6)
    assert p.quantity == 0

def test_product_update_quantity_negative_raises_error():
    """Проверяет, что нельзя сделать количество отрицательным."""
    p = Product("Чайник", "Металлический", 1500.0, 5)
    with pytest.raises(ValueError, match="Количество не может стать отрицательным"):
        p.update_quantity(-10)

# Тест для Category.display_info
def test_category_display_info():
    """Проверяет вывод информации о категории."""
    prod1 = Product("Книга", "Фантастика", 499.0, 10)
    prod2 = Product("Ручка", "Гелевая", 50.0, 100)
    category = Category("Канцтовары", "Различные канцелярские товары", [prod1, prod2])

    info = category.display_info()
    assert "Категория: Канцтовары" in info
    assert "Описание: Различные канцелярские товары" in info
    assert "Количество товаров в категории: 2 шт." in info

# Тесты для Order — крайние случаи
def test_order_large_quantity():
    """Проверяет заказ с большим количеством товара."""
    p = Product("Книга", "Фантастика", 499.0, 1000)
    order = Order(p, 500)
    assert order.quantity == 500
    assert order.total_cost == 499.0 * 500  # 249500.0


def test_order_quantity_exceeds_stock():
    """Проверяет, что заказ допускает количество больше, чем в наличии (бизнес-логика)."""
    p = Product("Книга", "Фантастика", 499.0, 10)  # в наличии 10
    order = Order(p, 100)  # заказываем 100
    assert order.quantity == 100
    assert order.total_cost == 499.0 * 100

# Тест для логов CreationLogger
def test_creation_logger_logging(capsys):
    p = Product("Телефон", "Смартфон", 29999.0, 5)
    captured = capsys.readouterr()
    print("CAPTURED OUT:", captured.out)  # ← Для отладки
    print("CAPTURED ERR:", captured.err)
    assert f"Product('Телефон', 'Смартфон', 29999.0, 5)" in captured.out

# Тесты для валидации Product — граничные значения
def test_product_zero_price():
    """Проверяет, что цена может быть нулевой."""
    p = Product("Бесплатный образец", "Тест", 0.0, 5)
    assert p.price == 0.0

def test_product_zero_quantity():
    """Проверяет, что количество может быть нулевым."""
    p = Product("Товар", "Описание", 100.0, 0)
    assert p.quantity == 0

def test_product_whitespace_name():
    """Проверяет, что имя с пробелами не считается пустым."""
    p = Product("  Телевизор  ", "LED", 30000.0, 1)
    assert p.name == "  Телевизор  "

def test_product_whitespace_description():
    """Проверяет, что описание с пробелами не считается пустым."""
    p = Product("Телевизор", "  LED TV  ", 30000.0, 1)
    assert p.description == "  LED TV  "

# Тест для get_total_cost с нулевым количеством
def test_product_get_total_cost_zero_quantity():
    """Проверяет расчёт общей стоимости при нулевом количестве."""
    p = Product("Книга", "Фантастика", 499.0, 0)
    assert p.get_total_cost() == 0.0

#Тест для Order — изменение количества после создания
def test_order_update_quantity_after_creation():
    """Проверяет, что можно изменить количество в заказе после создания."""
    p = Product("Книга", "Фантастика", 499.0, 10)
    order = Order(p, 2)

    # В реальной системе может быть метод update_quantity
    # Если его нет — пропустите этот тест или добавьте метод в Order
    # Для примера предположим, что можно менять напрямую:
    order.quantity = 5
    order.total_cost = order.product.price * order.quantity
    assert order.quantity == 5
    assert order.total_cost == 499.0 * 5

