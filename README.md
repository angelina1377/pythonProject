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
## Методы 
 
 | Метод          | Аргументы                                                                                                     | Описание                                                                      |
 |----------------|---------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------|
 | Class Product  | ```def __init__(self, name:str, description:str, price:float, quantity:int)```                                | Класс со свойствами                                                           |
 | Class Product  | ```def __add__(self, other)```                                                                                | Метод складывания товаров только из одинаковых классов продуктов              |
 | Class Category | ```def __init__(self,name:str, description:str,products:list, category_count = None,product_count = None )``` | Класс со свойствами                                                           |
 | Class Category | ```def add_product(self, product)```                                                                          | Метод, который добавляет product,если он экземпляр Product или его наследника |
## Модуль utils.py
 Модуль чтения из json файла и создание объектов классов
## Методы

| Метод                    | Аргументы                                  | Возвращаемый тип | Описание                                |
|--------------------------|--------------------------------------------|------------------|-----------------------------------------|
| read_json                | ```read_json``` str: Строка                | dict: Словарь    | Функция чтения из json файла            |
| create_objects_from_json | ```create_objects_from_json``` str: Строка |                  | Функция преобразования в объекты класса |

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

* Функция ```test_add_product_valid```:

* Функция ```test_add_non_product_raises_error```:

