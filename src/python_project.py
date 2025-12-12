class Product:
    name:str
    description:str
    price:float
    quantity:int

    def __init__(self, name:str, description:str, price:float, quantity:int):
        if price < 0:
            raise ValueError("Цена не может быть отрицательной")
        if quantity <0:
            raise ValueError("Количество не может быть отрицательным")
        self.name = name
        self.description = description
        self.price = price
        self.quantity = quantity

    def __add__(self, other):#
        #Проверяем, что other - того же класса, что и self
        if type(self) is not type(other):#type(self) возвращает класс 1 объекта(Smartphone)
                                         #type(other) класс 2 объекта is not строгое сравнение
                                         #Данный метод запрещает складывать смартфон и газонную траву
            raise TypeError("Нельзя складывать товары разных типов")
            # Создаём экземпляр класса БЕЗ вызова __init__
        new_product = self.__class__.__new__(self.__class__)#__new__ — это низкоуровневый метод создания экземпляра класса (вызывается до __init__)
            #self.__class__  # → класс Smartphone
            #self.__class__.__new__(self.__class__)  # → создаёт объект Smartphone без вызова __init__


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

class LawnGrass(Product):
    def __init__(self, name, description, price, quantity, country, germination_period, color):
        super().__init__(name, description, price, quantity)
        self.country = country
        self.germination_period = germination_period
        self.color = color

class Category:
    name:str
    description:str
    products:list
    category_count = 0
    product_count = 0

    def __init__(self,name:str, description:str,products:list, category_count = None,product_count = None ):
        self.name = name
        self.description = description
        self.products = []
        Category.category_count += 1
        # Добавляем начальные продукты, не увеличивая счётчик повторно
        for product in (products or []):
            if product not in self.products:
                self.products.append(product)
                Category.product_count += 1 #Увеличиваем при добавлении

    def add_product(self, product):
        """Добавляет, что product - если он экземпляр Product или его наследник"""
        if not isinstance(product, Product):
            #Возвращает False, если product - например, строка, число или другой класс
            raise TypeError("Можно добавлять только объекты класса Product или его наследников")
        if product not in self.products:
            self.products.append(product)
            Category.product_count += 1



if __name__ == '__main__':
    smartphone1 = Smartphone("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5, 95.5,
                         "S23 Ultra", 256, "Серый")
    smartphone2 = Smartphone("Iphone 15", "512GB, Gray space", 210000.0, 8, 98.2, "15", 512, "Gray space")
    smartphone3 = Smartphone("Xiaomi Redmi Note 11", "1024GB, Синий", 31000.0, 14, 90.3, "Note 11", 1024, "Синий")

    print(smartphone1.name)
    print(smartphone1.description)
    print(smartphone1.price)
    print(smartphone1.quantity)
    print(smartphone1.efficiency)
    print(smartphone1.model)
    print(smartphone1.memory)
    print(smartphone1.color)

    print(smartphone2.name)
    print(smartphone2.description)
    print(smartphone2.price)
    print(smartphone2.quantity)
    print(smartphone2.efficiency)
    print(smartphone2.model)
    print(smartphone2.memory)
    print(smartphone2.color)

    print(smartphone3.name)
    print(smartphone3.description)
    print(smartphone3.price)
    print(smartphone3.quantity)
    print(smartphone3.efficiency)
    print(smartphone3.model)
    print(smartphone3.memory)
    print(smartphone3.color)

    grass1 = LawnGrass("Газонная трава", "Элитная трава для газона", 500.0, 20, "Россия", "7 дней", "Зеленый")
    grass2 = LawnGrass("Газонная трава 2", "Выносливая трава", 450.0, 15, "США", "5 дней", "Темно-зеленый")

    print(grass1.name)
    print(grass1.description)
    print(grass1.price)
    print(grass1.quantity)
    print(grass1.country)
    print(grass1.germination_period)
    print(grass1.color)

    print(grass2.name)
    print(grass2.description)
    print(grass2.price)
    print(grass2.quantity)
    print(grass2.country)
    print(grass2.germination_period)
    print(grass2.color)

    smartphone_sum = smartphone1 + smartphone2
    print(smartphone_sum)

    grass_sum = grass1 + grass2
    print(grass_sum)

    try:
        invalid_sum = smartphone1 + grass1
    except TypeError:
        print("Возникла ошибка TypeError при попытке сложения")
    else:
        print("Не возникла ошибка TypeError при попытке сложения")

    category_smartphones = Category("Смартфоны", "Высокотехнологичные смартфоны", [smartphone1, smartphone2])
    category_grass = Category("Газонная трава", "Различные виды газонной травы", [grass1, grass2])

    category_smartphones.add_product(smartphone3)

    print(category_smartphones.products)

    print(Category.product_count)

    try:
        category_smartphones.add_product("Not a product")
    except TypeError:
        print("Возникла ошибка TypeError при добавлении не продукта")
    else:
        print("Не возникла ошибка TypeError при добавлении не продукта")