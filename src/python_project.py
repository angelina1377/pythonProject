class Product:
    name:str
    description:str
    _price:float
    quantity:int

    def __init__(self, name:str, description:str, price:float, quantity:int):
        self.name = name
        self.description = description
        self._price = price
        self.quantity = quantity

    @property # Геттер для получения текущей цены
    def price(self) -> float:
        return self._price

    @price.setter # Сеттер для установки цены с валидацией
    def price(self, value: float):
        # 1. Проверка цена <= 0
        if value <= 0:
            print("Цена не должна быть нулевая или отрицательная")
            return # Не меняем цену, выходим

        # 2. Если цена понижается (сравнение со старой ценой)
        if self._price is not None and value < self._price: # Проверяем что старая цена существует и новая цена меньше старой
            print(f"Цена снижается с {self._price} до {value}. Подтвердить? (y/n)")
            user_input = input(). strip(). lower()
            if user_input != 'y':
                print("Изменение цены отменено.")
                return # Не меняем цену, выходим
        # 3. Если все проверки пройдены - устанавливаем новую цену
        self._price = value
        print(f"Цена обновлена: {self._price}")

    @classmethod # Класс-метод принимает на вход параметры товара в словаре и возвращает объект класса
    def new_product(cls, product_data: dict, products_list: list = None ):
        """ Создаёт новый товар или обновляет существующий в списке
        product_data: dict: словарь с полями нового товара(name, description, price, quantity
        product_list: list: список существующих товаров для поиска дубликатов(опционально)
        Product: новый или обновленный объект товара"""

        # Значения извлекаются из product_data и сохраняются в переменные
        name = product_data['name']
        description = product_data['description']
        price = product_data['price']
        quantity = product_data['quantity']

        # Если список товаров не передан или пуст - просто создаем новый товар
        if not products_list:
            return cls(name, description, price, quantity)

        # Ищем товар с таким же именем в списке
        for existing_product in products_list:
            if existing_product.name == name:
                # Если товар найден - обновляем его:
                # - складываем количества
                existing_product.quantity += quantity
                # выбираем максимальную цену
                existing_product.price = max(existing_product.price, price)
                # обновляем описание
                existing_product.description = description
                return existing_product # возвращаем обновленный товар
         # Если товар не найден - создаем новый
        new_product = cls(name, description, price, quantity)
        products_list.append(new_product) # добавляем в список
        return new_product



class Category:
    name:str
    description:str
    products:list
    category_count = 0 # Счетчик всех созданных категорий(общий для всех экземпляров)
    product_count = 0 # Общий счетчик товаров во всех категориях(суммарно по всем экземплярам)

    def __init__(self,name:str, description:str,products:list, category_count = None,product_count = None ):
        self.name = name
        self.description = description
        # Создание приватного атрибута
        self.__products = products if products else []
        Category.category_count += 1
        # Обновляем общий счетчик товаров
        Category.product_count += len(self.__products)

    def add_product(self, product): # Метод позволяет безопасно добавлять товары в приватный список
        if not isinstance(product, Product): # Предотвращает ошибки (добавление строки или числа)
            raise TypeError("Можно добавлять только объекты класса Product")
        self.__products.append(product) # Добавляет товар в приватный список
        Category.product_count += 1 # Увеличиваем общий счетчик

    @property # Геттер безопасно получает данные из приватного списка
    def products(self):
        # Возвращаем список строк, где каждая строка - описание одного товара
        return [f'{product.name}, {product.price} руб. Остаток: {product.quantity} шт.' # Берет атрибуты name, price, quantity
                for product in self.__products]# Перебирает каждый объект товара в приватном списке



if __name__ == "__main__":
    product1 = Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5)
    product2 = Product("Iphone 15", "512GB, Gray space", 210000.0, 8)
    product3 = Product("Xiaomi Redmi Note 11", "1024GB, Синий", 31000.0, 14)

    category1 = Category(
        "Смартфоны",
        "Смартфоны, как средство не только коммуникации, но и получения дополнительных функций для удобства жизни",
        [product1, product2, product3]
    )

    print(category1.products)
    product4 = Product("55\" QLED 4K", "Фоновая подсветка", 123000.0, 7)
    category1.add_product(product4)
    print(category1.products)
    print(category1.product_count)

    new_product = Product.new_product(
        {"name": "Samsung Galaxy S23 Ultra", "description": "256GB, Серый цвет, 200MP камера", "price": 180000.0,
         "quantity": 5})
    print(new_product.name)
    print(new_product.description)
    print(new_product.price)
    print(new_product.quantity)

    new_product.price = 800
    print(new_product.price)

    new_product.price = -100
    print(new_product.price)
    new_product.price = 0
    print(new_product.price)