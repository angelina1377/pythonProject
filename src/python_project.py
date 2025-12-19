from abc import ABC, abstractmethod

class CreationLogger:# Класс-миксин, будет добавлять логирование создания объектов
    @staticmethod
    def log_creation(instance):
        class_name = instance.__class__.__name__
        attrs = ', '.join(repr(getattr(instance, attr)) for attr in instance.__dict__)
        print(f"{class_name}({attrs})")


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

class Product(CreationLogger, BaseProduct):
    name:str
    description:str
    price:float
    quantity:int

    def __init__(self, name: str, description: str, price: float, quantity: int):
        # Валидация входных данных
        if name is None or not name.strip():
            raise ValueError("Name не может быть None или пустым (после удаления пробелов)")
        if description is None or not description.strip():
            raise ValueError("Description не может быть None или пустым (после удаления пробелов)")
        if price < 0:
            raise ValueError("Цена не может быть отрицательной")
        if quantity < 0:
            raise ValueError("Количество не может быть отрицательным")

        # Инициализация атрибутов
        self.name = name
        self.description = description
        self.price = price
        self.quantity = quantity

        # Логирование через композицию
        CreationLogger.log_creation(self)

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
        if type(other) is not type(self):
            raise TypeError("Нельзя складывать товары разных типов")

            # Создаём новый экземпляр того же класса
        new_product = self.__class__(**self.__dict__)
        new_product.quantity += other.quantity
        return new_product

class Smartphone(Product):
    def __init__(self, name, description, price, quantity, efficiency, model, memory, color):
        # Сначала инициализируем базовые поля через Product.__init__
        super().__init__(name, description, price, quantity)

        # Затем устанавливаем специфические поля
        self.efficiency = efficiency
        self.model = model
        self.memory = memory
        self.color = color
        # Добавляем логирование создания
        print(f"Smartphone('{name}', '{description}', {price}, {quantity}, '{efficiency}', '{model}', '{memory}', '{color}')")

    def display_info(self) -> str:
        """Переопределённый метод отображения информации — специфичный для смартфонов."""
        return (f"{self.name} ({self.model}): {self.description}, "
                f"цена — {self.price} руб., память — {self.memory} ГБ, цвет — {self.color}, "
                f"в наличии — {self.quantity} шт.")

class LawnGrass(Product):
    def __init__(self, name, description, price, quantity, country, germination_period, color):
        # Сначала инициализируем базовые поля
        super().__init__(name, description, price, quantity)

        # Затем устанавливаем специфические поля
        self.country = country
        self.germination_period = germination_period
        self.color = color


    def display_info(self) -> str:
        """Переопределённый метод отображения информации — специфичный для газонной травы."""
        return (f"{self.name}: {self.description}, страна производства — {self.country}, "
                f"срок прорастания — {self.germination_period} дней, цвет — {self.color}, "
                f"цена — {self.price} руб., в наличии — {self.quantity} шт.")

class Order(BaseEntity):
    """Класс «Заказ»: хранит товар, количество и итоговую стоимость."""
    def __init__(self, product, quantity: int):
        if not isinstance(product, Product):
            raise TypeError("Товар должен быть экземпляром класса Product или его наследника")
        # Передаём name и description товара в BaseEntity
        super().__init__(name=product.name, description=product.description)

        self.product = product
        self.quantity = quantity
        self.total_cost = product.price * quantity
        # Логирование заказа
        CreationLogger.log_creation(self)

    def display_info(self) -> str:
        return (f"Заказ: {self.name}\n"
                f"Описание: {self.description}\n"
                f"Количество: {self.quantity} шт.\n"
                f"Итоговая стоимость: {self.total_cost} руб.")


class Category:
    category_count = 0
    product_count = 0

    def __init__(self,name:str, description:str,products:list, category_count = None,product_count = None ):
        self.name = name
        self.description = description
        self.products =  []
        Category.category_count += 1
        # Добавляем начальные продукты, не увеличивая счётчик повторно
        for product in products:
            self.add_product(product)

    def display_info(self) -> str:
        """Возвращает строку с информацией о категории."""
        product_count = len(self.products)
        return (f"Категория: {self.name}\n"
                f"Описание: {self.description}\n"
                f"Количество товаров в категории: {product_count} шт.")

    def add_product(self, product):
        """Добавляет продукт, если он экземпляр Product или его наследник."""
        if not isinstance(product, Product):
            raise TypeError("Можно добавлять только объекты класса Product или его наследников")

        # Проверка на дубликат: сравниваем ключевые поля
        for existing_product in self.products:
            if (existing_product.name == product.name and
                    existing_product.description == product.description and
                    existing_product.price == product.price):
                return  # Дубликат — не добавляем

        # Если не нашли дубликат — добавляем (вне цикла!)
        self.products.append(product)
        Category.product_count += 1


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