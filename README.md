# Project E-commerce
## Цель проекта: 
>Оценка навыков написания программы студента Skypro
## Описание: 
>Project E-commerce - это проект для ядро для интернет-магазина.В дальнейшем для этого ядра возможно будет реализовать любой интерфейс-от сайта до телеграм-бота
## Установка:
[Клонируйте репозиторий](https://github.com/angelina1377/pythonProject) 
## Установка Poetry
Если у Вас еще не установлен Poetry, выполните следующую команду:
[Poetry] (https://python-poetry.org/docs/#installing-with-the-official-installer)

После установки добавьте [Poetry] (https://python-poetry.org/docs/#installing-with-the-official-installer) в PATH
## Установка зависимостей
Используйте Poetry для создания виртуального окружения, включая инструменты разработки:flake8, isort, black, mypy:
poetry install
## Доступные модули и методы:
 * python_project.py 
 * utils.py 
 
## Модуль python_project.py 
 Модуль для создания классов Product и Category
| Метод                       | Аргументы                                                                                                     | Описание                                                                          |   
 |----------------------------|---------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------|
 | Class Product                           | ```def __init__(self, name:str, description:str, price:float, quantity:int)```                                | Класс со свойствами                                                               |
 | Class Product                           | ```def __add__(self, other)```                                                                                | Метод складывания товаров только из одинаковых классов продуктов                  |
 | Class Product                           | ``` def get_total_cost(self) -> float```                                                                      | Реализация абстрактного метода - вычисляет общую стоимость                        |
 | Class Product                           | ```def display_info(self) -> str```                                                                           | Реализация абстрактного метода - возвращает строку с инфо о товаре                |
 | Class Product                           | ```def update_quantity(self, amount: int) -> None```                                                          | Реализация абстрактного метода — обновляет количество товара                      |
 | Class Product                           | ```def update_quantity(self, amount: int) -> None```                                                          | Реализация абстрактного метода — обновляет количество товара                      |
 | class Order(BaseEntity)                 | ```def __init__(self, product, quantity: int)```                                                              | Класс «Заказ»: хранит товар, количество и итоговую стоимость                      |
 | class Smartphone(Product)               | ```def __init__(self, name, description, price, quantity, efficiency, model, memory, color)```                | Класс наследник  от исходного класса  Product                                     |
 | class LawnGrass(Product)                | ```def __init__(self, name, description, price, quantity, country, germination_period, color) ```             | Класс наследник  от исходного класса  Product                                     |
 | Class Category                          | ```def add_product(self, product)```                                                                          | Метод, который добавляет product,если он экземпляр Product или его наследника     |
 | Class Category                          | ```def middle_price(self) -> float```                                                                         | Метод, который подсчитывает средний ценник всех товаров в категории               |
 | Class CreationLogger                    | ```def log_creation```                                                                                        | Класс-миксин, будет добавлять логирование создания объектов(доп.функциональность) |
 | Class BaseProduct(ABC)                  | ```def get_total_cost(self)```                                                                                | Метод, который Возвращает общую стоимость товара (цена * количество)              |
 | Class BaseProduct(ABC)                  | ```def display_info(self)```                                                                                  | Метод, который Отображает основную информацию о товаре                            |
 | Class BaseProduct(ABC)                  | ```def update_quantity(self, amount: int)```                                                                  | Метод, который Обновляет количество товара                                        |
 | Class  BaseEntity(ABC)                  | ```def __init__(self, name: str, description: str)```                                                         | Абстрактный базовый класс, который создает шаблон для наследников: __init__ инициализирует name — название сущности и description — описание сущности|
 | Class  BaseEntity(ABC)                  | ```def display_info(self) -> str```                                                                           | Метод, который задает единый интерфейс для вывода информации о сущности|
 | Class  BaseEntity(ABC)                  | ```def __str__(self) -> str```                                                                                | Метод, который определяет как объект будет преобразовываться в строку, просто возвращает результат display_info()|
 | Class ZeroQuantityError(Exception)      | ```def __init__(self, message="Товар с нулевым количеством не может быть добавлен")```                        | Класс исключение для случая, когда товар имеет нулевое количество|
## Модуль utils.py
 Модуль чтения из json файла и создание объектов классов
## Методы

| Метод                    | Аргументы                                  | Возвращаемый тип | Описание                                |
|--------------------------|--------------------------------------------|------------------|-----------------------------------------|
| read_json                | ```read_json``` str: Строка                | dict: Словарь    | Функция чтения из json файла            |
| create_objects_from_json | ```create_objects_from_json``` str: Строка |                  | Функция преобразования в объекты класса |


# Тестирование
# Тестирование
### Модуль python_project.py
* Функция ```test_product_creation```:
-Тестирование правильности установки атрибутов объекта
* Функция ```test_category_creation_with_products```:
Тестирование правильности атрибутов категории
* Функция ```test_category_counters```:
Тестирование правильности работы счетчиков
* Функция ```test_category_empty_products```:
Тестирование правильности работы с пустой категорией
* Функция ```test_product_addition_same_type```:
Тестирование сложения двух объектов Product одного типа (одинаковые название, цена, описание)
* Функция ```test_product_addition_different_types_raises_error```:
Тестирование попытки сложить Product и Smartphone (разные классы).
* Функция ```test_smartphone_creation```:
Тестирование корректности создания объекта Smartphone
* Функция ```test_smartphone_addition```:
Тестируется сложение двух Smartphone с одинаковыми характеристиками
* Функция ```test_lawngrass_creation```:
Тестирование создание объекта класса LawnGrass
* Функция ```test_lawngrass_addition```:
Тестирование сложения двух LawnGrass с одинаковыми параметрами
* Функция ```test_add_product_valid```:
Тестирование добавления корректного продукта (Smartphone) в категорию
*  Функция ```test_add_non_product_raises_error```:
Тестирование попытки добавить в категорию не объекты Product (строку, число, словарь) 
* Функция ```test_lawngrass_addition```:
Тестирование сложения двух LawnGrass с одинаковыми параметрами
* Функция ```test_add_product_valid```:
Тестирование добавления продукта в список category.products
* Функция ```test_add_non_product_raises_error```
Тестирование добавления в категорию не объекты Product (строку, число, словарь)
* Функция ```def test_product_negative_quantity_raises_error()```
Тестирование на отрицательные quantity и price
* Функция ```def test_product_negative_price_raises_error()```
Тестирование на то, что отрицательная price вызывает ошибку
* Функция ```def test_smartphone_addition_copies_all_attributes()```
Тестирование копирования всех атрибутов в __add__(для наследников)
* Функция ```def test_add_product_invalid_types()```
Тестирование на isinstance с крайними случаями
* Функция ```def test_add_product_invalid_types()```
Тестирование на isinstance с крайними случаями
* Функция ```def test_product_negative_price()```
Тестирование того, что при отрицательной цене товара (-100.0) выбрасывается исключение ValueError с корректным сообщением
* Функция ```def test_product_negative_quantity()```
Тестирование того, что отрицательное количество (-5) вызывает ValueError с ожидаемым текстом ошибки
* Функция ```def test_add_different_types_raises_error()```
Тестирует запрет на сложение разных типов товаров (Product + Smartphone) — должно быть TypeError
* Функция ```def test_add_non_product_raises_error()```
Тестирует, что в категорию нельзя добавить не‑товар (строку, число и т. п.) — ожидается TypeError
* Функция ```def test_category_init_with_products()```
Тестирует, что в что при создании категории со списком товаров: все товары добавлены в products,счётчик product_count увеличен корректно (без дублирования) 
* Функция ```def test_smartphone_specific_fields()```
Тестирует наличие и корректность специфических полей Smartphone (efficiency, model)
* Функция ```def test_lawngrass_specific_fields()```
Тестирует поля country, germination_period
* Функция ```def test_add_duplicate_product()```
Тестирует, что дубликат товара не добавляется в категорию, а счётчик product_count не увеличивается
* Функция ```def test_product_creation()```
Тестирует корректную инициализацию объекта Product (все атрибуты сохранены верно)
* Функция ```def test_product_negative_price(def test_product_empty_strings()```
Тестирует валидацию: пустая строка для name или description должна вызывать ValueError
* Функция ```def test_product_none_values()```
Тестирует реакцию на None в name/description — ожидается ValueError
* Функция ```def test_smartphone_creation()```
Тестирует корректную инициализацию Smartphone (все поля, включая специфические, заданы)
* Функция ```def test_smartphone_addition()```
Тестирует сложение двух Smartphone: количество суммируется,тип результата — Smartphone, сохраняются специфические поля
* Функция ```def test_lawngrass_creation()```
Тестирует инициализации всех полей
* Функция ```def test_lawngrass_addition()```
Тестирует сложение двух LawnGrass (сумма количеств, сохранение полей)
* Функция ```def test_category_creation_with_products()```
Тестирует, что категория с начальным списком товаров содержит их все
* Функция ```def test_category_counters()```
Тестирует, что корректность счётчиков category_count и product_count при создании категории и добавлении товара
* Функция ```def test_category_empty_products()```
Тестирует создание категории без товаров: список products пуст, счётчики не увеличены
* Функция ```def test_add_product_valid()```
Тестирует добавление корректного товара в категорию (товар в списке, счётчик увеличен)
* Функция ```def test_order_creation()```
Тестирует правильную инициализацию заказа
* Функция ```def test_order_invalid_product()```
Тестирует запрет на создание заказа с некорректным товаром (None, строка, число) — TypeError
* Функция ```def test_order_zero_quantity()```
Тестирует заказ с нулевым количеством (стоимость = 0)
* Функция ```def test_order_display_info()```
Тестирует формат вывода информации о заказе через display_info()
* Функция ```def test_order_str_representation()```
Тестирует что str(order) совпадает с display_info()
* Функция ```def test_order_total_cost_calculation()```
Тестирует расчёт total_cost при заданном количестве
* Функция ```def test_order_hash()```
Тестирует возможность использования заказа в множествах/словарях (хеширование)
* Функция ```def test_full_workflow()```
Тестирует цепочку «продукт → категория → заказ» на согласованность
* Функция ```def test_product_update_quantity()```
Тестирует изменение количества товара
* Функция ```def test_product_update_quantity_negative_raises_error()```
Тестирует запрет на установку отрицательного количества через update_quantity()
* Функция ```def test_category_display_info()```
Тестирует корректность вывода информации о категории (название, описание, количество товаров)
* Функция ```def test_order_large_quantity()```
Тестирует заказ с большим количеством товара (расчёт стоимости)
* Функция ```def test_order_quantity_exceeds_stock()```
Тестирует, что заказ допускает количество больше, чем в наличии (бизнес‑логика)
* Функция ```def test_product_zero_price()```
Тестирует допустимость нулевой цены товара
* Функция ```test_middle_price_single_product()```
Тестирует допустимость нулевого количества товара
* Функция ```def test_product_whitespace_name()```
Тестирует, что имя с пробелами не считается пустым (валидация)
* Функция ```def test_product_whitespace_description()```
Тестирует, что описание с пробелами не считается пустым (валидация)
* Функция ```def test_product_get_total_cost_zero_quantity()```
Тестирует расчёт общей стоимости при нулевом количестве (должно быть 0.0)
* Функция ```def test_order_update_quantity_after_creation()```
Тестирует изменение количества в заказе после его создания (пересчёт стоимости)
* Функция ```def test_middle_price_single_product()```
Тестирует базовый случай: 1 товар → средний = цене товара
* Функция ```def test_middle_price_multiple_products()```
Тестирует расчёт для нескольких товаров с разными ценами
* Функция ```def test_middle_price_empty_category()```
Тестирует что пустая категория возвращает 0.0 (обработка ZeroDivisionError)
* Функция ```def test_middle_price_with_zero_quantity_products()```
Тестирует количество товара (quantity) не влияет на расчёт среднего (учитывается только price)
* Функция ```def test_middle_price_identical_prices()```
Тестирует что при одинаковых ценах результат равен этой цене.
* Функция ```def test_middle_price_decimal_precision()```
Тестирует точность вычислений для дробных значений
* Функция ```def test_middle_price_large_numbers()```
Тестирует работу с крупными суммами (исключает переполнение)
* Функция ```def test_middle_price_after_product_removal()```
Тестирует что метод корректно реагирует на изменение списка products.