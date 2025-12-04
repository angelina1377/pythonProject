class Product:
    name:str
    description:str
    price:float
    quantity:int

    def __init__(self, name:str, description:str, price:float, quantity:int):
        self.name = name
        self.description = description
        self.price = price
        self.quantity = quantity

    def __str__(self):
        return f'Название продукта:{self.name}, {self.price} руб. Остаток: {self.quantity} шт.'

    def __add__(self, other):
        if not isinstance(other, Product):
            raise TypeError("Можно складывать только объекты класса Product")
        total_value = self.price * self.quantity + other.price * other.quantity
        return total_value


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
        Category.product_count = len(products)

    def __str__(self):
        total_quantity = sum(product.quantity for product in self.products) # Проходим по всем продуктам в self.products
                                                                            # берет у каждого атрибут quantity
                                                                            # суммирует все значения
        return f'Название категории:{self.name}, количество продуктов: {total_quantity} шт.'


class CategoryIterator:
    """
    Итератор для последовательного обхода товаров в категории.

    Позволяет использовать цикл `for` для перебора продуктов:
        for product in CategoryIterator(category):
            print(product)
    """

    def __init__(self, category):
        """
        Инициализация итератора.

        :param category: объект класса Category, чьи продукты нужно перебирать
        """
        self.category = category
        self._index = 0  # Текущая позиция в списке продуктов

    def __iter__(self):
        """
        Метод __iter__ возвращает сам итератор (обычно self).
        Требуется для протокола итерации в Python.
        """
        return self

    def __next__(self):
        """
        Возвращает следующий товар из категории.

        :return: объект Product
        :raises StopIteration: если все товары уже перебраны
        """
        # Проверяем, не вышли ли за границы списка продуктов
        if self._index >= len(self.category.products):
            raise StopIteration

        # Получаем текущий продукт и увеличиваем индекс
        product = self.category.products[self._index] #Получает текущий товар из списка products категории по текущему индексу
                                                      # self.category - ссылка на объект категории переданный при создании итератора
                                                      # .products - список товаров внутри этой категории [prod1, prod2]
                                                     # [self._index] обращение к элементу списка по индексу если self._index =0 берем prod1
                                                     # если self._index = 1 то берем (prod2)
        self._index += 1 # Увеличивает индекс на 1, чтобы при следующем вызове __next__ вернуться к следующему товару.

        return product


# if __name__ == "__main__":
#     product1 = Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5)
#     product2 = Product("Iphone 15", "512GB, Gray space", 210000.0, 8)
#     product3 = Product("Xiaomi Redmi Note 11", "1024GB, Синий", 31000.0, 14)
#
#     print(product1.name)
#     print(product1.description)
#     print(product1.price)
#     print(product1.quantity)
#
#     print(product2.name)
#     print(product2.description)
#     print(product2.price)
#     print(product2.quantity)
#
#     print(product3.name)
#     print(product3.description)
#     print(product3.price)
#     print(product3.quantity)
#
#     category1 = Category("Смартфоны",
#                          "Смартфоны, как средство не только коммуникации, но и получения дополнительных функций для удобства жизни",
#                          [product1, product2, product3])
#
#     print(category1.name == "Смартфоны")
#     print(category1.description)
#     print(len(category1.products))
#     print(category1.category_count)
#     print(category1.product_count)
#
#     product4 = Product("55\" QLED 4K", "Фоновая подсветка", 123000.0, 7)
#     category2 = Category("Телевизоры",
#                          "Современный телевизор, который позволяет наслаждаться просмотром, станет вашим другом и помощником",
#                          [product4])
#
#     print(category2.name)
#     print(category2.description)
#     print(len(category2.products))
#     print(category2.products)
#
#     print(Category.category_count)
#     print(Category.product_count)

if __name__ == '__main__':
    product1 = Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5)
    product2 = Product("Iphone 15", "512GB, Gray space", 210000.0, 8)
    product3 = Product("Xiaomi Redmi Note 11", "1024GB, Синий", 31000.0, 14)

    print(str(product1))
    print(str(product2))
    print(str(product3))

    category1 = Category(
        "Смартфоны",
        "Смартфоны, как средство не только коммуникации, но и получения дополнительных функций для удобства жизни",
        [product1, product2, product3]
    )

    print(str(category1))

    print(category1.products)

    print(product1 + product2)
    print(product1 + product3)
    print(product2 + product3)