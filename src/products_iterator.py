# from src.product_and_category import Product, Category


class ProductsIterator:
    '''Вспомогательный класс, с помощью которого можно перебирать товары одной категории,
    например в цикле for. Принимает на вход объект класса категории и производит итерацию по товарам,
    которые хранятся в данной категории.'''

    def __init__(self, object_category):
        self.category = object_category
        self.index = 0

    def __iter__(self):
        self.index = 0
        return self

    def __next__(self):
        if self.index < len(self.category.products_in_list):
            prod = self.category.products_in_list[self.index]
            self.index += 1
            return prod
        else:
            raise StopIteration


# if __name__ == '__main__':
#     product1 = Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5)
#     product2 = Product("Iphone 15", "512GB, Gray space", 210000.0, 8)
#     product3 = Product("Xiaomi Redmi Note 11", "1024GB, Синий", 31000.0, 14)
#
#     category1 = Category(
#         "Смартфоны",
#         "Смартфоны, как средство не только коммуникации, но и получения дополнительных функций для удобства жизни",
#         [product1, product2, product3]
#     )
#
#     iterator = ProductsIterator(category1)
#     for product in iterator:
#         print(product)
#     print()
#     for product in iterator:
#         print(product)
