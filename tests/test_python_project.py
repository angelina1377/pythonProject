import pytest

from src.python_project import Product, Category

@pytest.fixture(autouse=True)
def reset_category_counts():
    Category.category_count = 0
    Category.product_count = 0


def test_product_creation():
    """Проверка создания объекта Product с корректными данными.
    Убедиться, что конструктор __init__ корректно устанавливает все"""
    p = Product("Телефон", "Смартфон с 128 ГБ", 29999.0, 5)
    assert p.name == "Телефон"
    assert p.description == "Смартфон с 128 ГБ"
    assert p.price == 29999.0
    assert p.quantity == 5

def test_price_getter():
    """Проверка геттера price:Проверяем, что геттер возвращает сохраненное значение"""
    p = Product("Товар", "Описание", 100.0, 1)
    assert p.price == 100.0

def test_set_positive_price():
    """Установка положительной цены: проверяем, что цена обновилась.
     Чтобы убедиться, что сеттер позволяет менять цену на большую"""
    p = Product("Товар", "Описание", 100.0, 1)
    p.price = 150.0
    assert p.price == 150.0

def test_set_zero_price():
    """Проверить валидацию: Цена ≤ 0 — не должна приниматься, проверяем, что остаётся старая цена."""
    p = Product("Товар", "Описание", 100.0, 1)
    p.price = 0
    assert p.price == 100.0  # не изменилась

def test_set_negative_price():
    """Проверка запрета отрицательной цены. Отрицательная цена — не обновляется."""
    p = Product("Товар", "Описание", 100.0, 1)
    p.price = -10.0
    assert p.price == 100.0  # не изменилась

def test_new_product_without_list():
    """new_product без списка — возвращает новый объект."""
    data = data = {
    'name': 'Ноутбук',
    'description': 'Игровой',
    'price': 79999.0,
    'quantity': 2
}
  # словарь с данными товара
    product = Product.new_product(data)
    assert isinstance(product, Product)  # это объект Product(метод класса, который должен создать объект)?
    # Проверяем вернулся ли объект типа Product и правильные ли у него атрибуты
    assert product.name == "Ноутбук"
    assert product.price == 79999.0
    assert product.quantity == 2

def test_new_product_update_existing():
    """new_product обновляет существующий товар в списке.
    Создаем существующий товар и кладем в список
    new_product должен обновить существующий товар
     Проверяем: кол-во суммировалось (3+4=7)
                цена взята максимальная(31999.0 > 29999.0)
                описание обновилось
                логику обновления существующего товара"""
    existing = Product("Смартфон", "Старый описание", 29999.0, 3)
    products = [existing]  # список с одним товаром

    data = {
        'name': 'Смартфон',  # должно совпадать!
        'description': 'Обновлённое описание',
        'price': 31999.0,
        'quantity': 4
    }
  # новые данные для того же товара (имя совпадает)

    updated = Product.new_product(data, products)


    assert updated.quantity == 7      # 3 + 4
    assert updated.price == 31999.0     # новая цена выше — берём её
    assert updated.description == "Обновлённое описание"

def test_new_product_add_new():
    """new_product добавляет новый товар в список, если его нет.
    Проверяем: увеличение длины списка
               новый товар имеет праильные атрибуты
               новый товар добавлен в список
               метод добавляет новый товар, если его еще нет в списке"""
    products = [Product("Смартфон", "Описание", 29999.0, 3)]
    data = {
        'name': 'Наушники',  # как в assert!
        'description': 'Беспроводные',
        'price': 4999.0,
        'quantity': 5
    }
  # данные для нового товара (другое имя)

    new_product = Product.new_product(data, products)

    assert len(products) == 2        # в списке теперь 2 товара
    assert new_product.name == "Наушники"
    assert new_product in products


def test_category_creation_empty_products():
    """Проверка создания категории с пустым списком товаров и счетчиков."""
    cat = Category("Электроника", "Все для дома", [])

    assert cat.name == "Электроника"
    assert cat.description == "Все для дома"
    assert cat.products == []  # проверяем, что геттер возвращает пустой список
    assert Category.category_count == 1
    assert Category.product_count == 0


def test_category_creation_with_products():
    """Создание категории с начальным списком товаров."""
    cat = Category("Бытовая техника", "Для дома и кухни", [])

    p1 = Product("Телевизор", "4K Smart TV", 49999.0, 3)
    p2 = Product("Пылесос", "Робот-пылесос", 24999.0, 5)

    cat.add_product(p1)
    cat.add_product(p2)

    assert cat.name == "Бытовая техника"
    assert len(cat.products) == 2  # два товара в списке
    assert "Телевизор, 49999.0 руб. Остаток: 3 шт." in cat.products
    assert "Пылесос, 24999.0 руб. Остаток: 5 шт." in cat.products
    assert Category.category_count == 1
    assert Category.product_count == 2  # 2 товара суммарно


def test_add_product_valid():
    """Добавление корректного товара через add_product: проверка корректного добавления товара и обновления счетчика."""
    cat = Category("Книги", "Художественная литература", [])
    p = Product("Война и мир", "Роман-эпопея", 899.0, 10)

    cat.add_product(p)
    print(Category.category_count)
    assert len(cat.products) == 1
    assert "Война и мир, 899.0 руб. Остаток: 10 шт." in cat.products
    assert Category.product_count == 1  # общий счетчик увеличился


def test_add_product_invalid_type():
    """Попытка добавить не-Product — должно вызвать TypeError."""
    cat = Category("Одежда", "Мужская и женская", [])

    try:
        cat.add_product("не товар")  # строка вместо Product
        assert False, "Не возникло исключение TypeError"
    except TypeError as e:
        assert str(e) == "Можно добавлять только объекты класса Product"
    print(Category.category_count)
    assert len(cat.products) == 0 # Убеждаемся, что список товаров не изменился
    assert Category.product_count == 0 # Убеждается, что счетчик не увеличился


def test_products_getter_format():
    """Проверка формата строк, возвращаемых геттером products."""
    p = Product("Кофемашина", "Автоматическая", 19999.0, 7)
    cat = Category("Кухня", "Техника для приготовления", [p])

    result = cat.products  # вызываем геттер

    assert len(result) == 1 # проверяем длину списка
    expected = "Кофемашина, 19999.0 руб. Остаток: 7 шт." # проверяем что строка имеет ожидаемый формат
    assert result[0] == expected


def test_multiple_categories_count():
    """Проверка счетчиков category_count и product_count при создании нескольких категорий."""
    cat1 = Category("Спорт", "Инвентарь", [])
    assert Category.category_count == 1
    assert Category.product_count == 0

    p1 = Product("Мяч", "Футбольный", 999.0, 20)
    p2 = Product("Ракетка", "Теннисная", 2999.0, 15)

    cat2 = Category("Теннис", "Снаряжение", [])
    cat2.add_product(p1)
    cat2.add_product(p2)

    assert Category.category_count == 2
    assert Category.product_count == 2

    p3 = Product("Гантели", "Набор", 4999.0, 5) # Добавляем товар в 1 категорию
    cat1.add_product(p3)
    assert Category.product_count == 3

