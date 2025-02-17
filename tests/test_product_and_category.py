from src.product_and_category import Category
from tests.conftest import reset_category_counts


def test_product1_init(product1):
    assert product1.name == "Samsung Galaxy S23 Ultra"
    assert product1.description == "256GB, Серый цвет, 200MP камера"
    assert product1.price == 180000.0
    assert product1.quantity == 5


def test_product2_init(product2):
    assert product2.name == "Iphone 15"
    assert product2.description == "512GB, Gray space"
    assert product2.price == 210000.0
    assert product2.quantity == 8


def test_product3_init(product3):
    assert product3.name == "Xiaomi Redmi Note 11"
    assert product3.description == "1024GB, Синий"
    assert product3.price == 31000.0
    assert product3.quantity == 14


def test_product4_init(product4):
    assert product4.name == "55\" QLED 4K"
    assert product4.description == "Фоновая подсветка"
    assert product4.price == 123000.0
    assert product4.quantity == 7


def test_category1_init(category1, product1, product2, product3):
    assert category1.name == "Смартфоны"
    assert category1.description == ("Смартфоны, как средство не только коммуникации, но и "
                                     "получения дополнительных функций для удобства жизни")
    assert category1.products == [product1, product2, product3]


def test_category2_init(category2, product4):
    assert category2.name == "Телевизоры"
    assert category2.description == ("Современный телевизор, который позволяет наслаждаться "
                                     "просмотром, станет вашим другом и помощником")
    assert category2.products == [product4]


def test_category_count(category1, category2):
    assert Category.category_count == 2
    reset_category_counts()


def test_product_count(category1, category2):
    assert Category.product_count == 4
    reset_category_counts()
