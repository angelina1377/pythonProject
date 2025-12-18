from abc import ABC, abstractmethod


class CreationLogger:# Класс-миксин, будет добавлять логирование создания объектов
    def __init__(self, *args, **kwargs):# Собирает позиционные аргументы(name, price) в кортеж
                                    # Собирает именованные аргументы(red) в словарь
        class_name = self.__class__.__name__# Получаем имя класса для создаваемого объекта
                                            # self.__class__- например 'Smartphone'
        args_str = ', '.join([repr(arg) for arg in args])
        # Формируем строку из позиционных аргументов: [repr(arg) for arg in args] — список, где каждый аргумент преобразуется в строку через repr()
        # (даёт «официальное» строковое представление, например, 'iPhone' вместо iPhone).
        # ', '.join(...) — соединяет элементы списка через запятую и пробел.
        # Пример: если args = ('iPhone', 999), то args_str станет 'iPhone', 999'.
        kwargs_str = ', '.join([f"{k}={repr(v)}" for k, v in kwargs.items()])
        # Формирует строку из именованных аргументов.kwargs.items() — пары (ключ, значение) из словаря kwargs
        # Для каждой пары создаётся строка вида ключ=repr(значение) (например, color='gray').
        # Соединяет все такие строки через запятую и пробел.
        # Пример: если kwargs = {'color': 'gray'}, то kwargs_str станет color='gray'
        params_str = f"{args_str}, {kwargs_str}" if args_str and kwargs_str else args_str or kwargs_str
        # Собирает полную строку параметров для вывода.Если есть и args_str, и kwargs_str, соединяет их через запятую: 'iPhone', 999, color='gray'
        # Если только args_str — берёт его Если только kwargs_str — берёт его.
        # Это нужно, чтобы не было лишних запятых (например, когда нет позиционных аргументов).
        print(f"{class_name}({params_str})")# Выводит в консоль строку: Smartphone('iPhone', 999, color='gray')
        super().__init__(*args, **kwargs)# Вызывает конструктор родительского класса (следующего в цепочке наследования).
        #  Передаёт все полученные аргументы (*args, **kwargs) дальше


class BaseProduct(ABC):
    "Абстрактный класс для продуктов - определяет общую функциональность"

    @abstractmethod
    def get_total_cost(self) -> float:
        "Возвращает общую стоимость товара (цена * количество)"
        pass

    @abstractmethod
    def display_info(self) -> str:
        "Отображает основную информацию о товаре. Должен быть реализован в наследниках"
        pass

    @abstractmethod
    def update_quantity(self, amount: int) -> None:
        "Обновляет количество товара. Должен быть реализован в наследниках"
        pass

class BaseEntity(ABC):
    """Абстрактный базовый класс для сущностей с именем и описанием (Order, Category)."""
    def __init__(self, name: str, description: str):
        self.name = name
        self.description = description

    @abstractmethod
    def display_info(self) -> str:
        pass

    def __str__(self) -> str:
        return self.display_info()

class Product:
    name:str
    description:str
    price:float
    quantity:int


    def __init__(self, name: str, description: str, price: float, quantity: int):
        if price < 0:
            raise ValueError("Цена не может быть отрицательной")
        if quantity < 0:
            raise ValueError("Количество не может быть отрицательным")
        self.name = name
        self.description = description
        self.price = price
        self.quantity = quantity

    def get_total_cost(self) -> float:
        "Реализация абстрактного метода - вычисляет общую стоимость"
        return self.price * self.quantity


    def display_info(self) -> str:
        "Реализация абстрактного метода - возвращает строку с инфо о товаре"
        return f"{self.name}: {self.description}, цена - {self.price} руб., в наличии - {self.quantity} шт."

    def update_quantity(self, amount: int) -> None:
        """Реализация абстрактного метода — обновляет количество товара."""
        if self.quantity + amount < 0:
            raise ValueError("Количество не может стать отрицательным")
        self.quantity += amount

    def __add__(self, other):  #
        # Проверяем, что other - того же класса, что и self
        if type(self) is not type(other):  # type(self) возвращает класс 1 объекта(Smartphone)
            # type(other) класс 2 объекта is not строгое сравнение
            # Данный метод запрещает складывать смартфон и газонную траву
            raise TypeError("Нельзя складывать товары разных типов")
            # Создаём экземпляр класса БЕЗ вызова __init__
        new_product = self.__class__.__new__(
            self.__class__)  # __new__ — это низкоуровневый метод создания экземпляра класса (вызывается до __init__)
        # self.__class__  # → класс Smartphone
        # self.__class__.__new__(self.__class__)  # → создаёт объект Smartphone без вызова __init__

        # Проходит по всем парам(ключ, значения) и копируем ВСЕ атрибуты в новый объект
        for key, value in self.__dict__.items():
            setattr(new_product, key, value)

            # Обновляем только quantity (суммируем)
            # Все остальные атрибуты(имя, цена, модель и т.д.) остаются как у self
        new_product.quantity = self.quantity + other.quantity

        return new_product

class Smartphone(Product):
    def __init__(self, name, description, price, quantity, efficiency, model, memory, color):
        super().__init__(name, description, price, quantity)
        self.efficiency = efficiency
        self.model = model
        self.memory = memory
        self.color = color

    def display_info(self) -> str:
        """Переопределённый метод отображения информации — специфичный для смартфонов."""
        return (f"{self.name} ({self.model}): {self.description}, "
                f"цена — {self.price} руб., память — {self.memory} ГБ, цвет — {self.color}, "
                f"в наличии — {self.quantity} шт.")

class LawnGrass(Product):
    def __init__(self, name, description, price, quantity, country, germination_period, color):
        super().__init__(name, description, price, quantity)
        self.country = country
        self.germination_period = germination_period
        self.color = color

    def display_info(self) -> str:
        """Переопределённый метод отображения информации — специфичный для газонной травы."""
        return (f"{self.name}: {self.description}, страна производства — {self.country}, "
                f"срок прорастания — {self.germination_period} дней, цвет — {self.color}, "
                f"цена — {self.price} руб., в наличии — {self.quantity} шт.")

class Order(CreationLogger, BaseEntity):
    """Класс «Заказ»: хранит товар, количество и итоговую стоимость."""
    def __init__(self, product, quantity: int):
        if not isinstance(product, Product):
            raise TypeError("Товар должен быть экземпляром класса Product или его наследника")
        # Передаём name и description товара в BaseEntity
        super().__init__(name=product.name, description=product.description)
        self.product = product
        self.quantity = quantity
        self.total_cost = product.price * quantity

    def display_info(self) -> str:
        return (f"Заказ: {self.name}\n"
                f"Описание: {self.description}\n"
                f"Количество: {self.quantity} шт.\n"
                f"Итоговая стоимость: {self.total_cost} руб.")


class Category:
    name:str
    description:str
    products:list
    category_count = 0
    product_count = 0

    def __init__(self,name:str, description:str,products:list, category_count = None,product_count = None ):
        self.name = name
        self.description = description
        self.products = products if products else []
        Category.category_count += 1
        # Добавляем начальные продукты, не увеличивая счётчик повторно
        if products:
            for product in products:
                self.add_product(product)

    def add_product(self, product):
        """Добавляет, что product - если он экземпляр Product или его наследник"""
        if not isinstance(product, Product):
            # Возвращает False, если product - например, строка, число или другой класс
            raise TypeError("Можно добавлять только объекты класса Product или его наследников")
            # Ручная проверка на дубликат: сравниваем поля
        is_duplicate = False
        for existing_product in self.products:
            if (existing_product.name == product.name and
                    existing_product.description == product.description and
                    existing_product.price == product.price and
                    existing_product.quantity == product.quantity):
                is_duplicate = True
                break

            # Если продукта с такими же полями нет — добавляем
        if not is_duplicate:
            self.products.append(product)
            Category.product_count += 1

        def display_info(self) -> str:
            product_count = len(self.products)
            return (f"Категория: {self.name}\n"
                    f"Описание: {self.description}\n"
                    f"Количество товаров в категории: {product_count} шт.")


if __name__ == '__main__':
    product1 = Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5)
    product2 = Product("Iphone 15", "512GB, Gray space", 210000.0, 8)
    product3 = Product("Xiaomi Redmi Note 11", "1024GB, Синий", 31000.0, 14)

    print(product1.name)
    print(product1.description)
    print(product1.price)
    print(product1.quantity)

    print(product2.name)
    print(product2.description)
    print(product2.price)
    print(product2.quantity)

    print(product3.name)
    print(product3.description)
    print(product3.price)
    print(product3.quantity)

    category1 = Category("Смартфоны",
                         "Смартфоны, как средство не только коммуникации, но и получения дополнительных функций для удобства жизни",
                         [product1, product2, product3])

    print(category1.name == "Смартфоны")
    print(category1.description)
    print(len(category1.products))
    print(category1.category_count)
    print(category1.product_count)

    product4 = Product("55\" QLED 4K", "Фоновая подсветка", 123000.0, 7)
    category2 = Category("Телевизоры",
                         "Современный телевизор, который позволяет наслаждаться просмотром, станет вашим другом и помощником",
                         [product4])

    print(category2.name)
    print(category2.description)
    print(len(category2.products))
    print(category2.products)

    print(Category.category_count)
    print(Category.product_count)