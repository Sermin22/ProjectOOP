import pytest
from src.product_and_category import Product, Category


@pytest.fixture
def product1():
    return Product(
        name="Samsung Galaxy S23 Ultra",
        description="256GB, Серый цвет, 200MP камера",
        price=180000.0,
        quantity=5
    )


@pytest.fixture
def product2():
    return Product(
        name="Iphone 15",
        description="512GB, Gray space",
        price=210000.0,
        quantity=8
    )


@pytest.fixture
def product3():
    return Product(
        name="Xiaomi Redmi Note 11",
        description="1024GB, Синий",
        price=31000.0,
        quantity=14
    )


@pytest.fixture(scope='function')
def product4():
    return Product(
        name="55\" QLED 4K",
        description="Фоновая подсветка",
        price=123000.0,
        quantity=7
    )


def reset_category_counts():
    '''Функция предназначена для сброса статических переменных category_count и product_count
    класса Category. Она вызывается в фикстуре category после завершения теста'''
    Category.category_count = 0
    Category.product_count = 0


@pytest.fixture(scope='function')  # создает новую категорию для каждого теста отдельно
def category1(product1, product2, product3):
    # использование yield в фикстуре позволяет выполнять очистку после завершения теста
    yield Category(
        name="Смартфоны",
        description="Смартфоны, как средство не только коммуникации, но и получения "
                    "дополнительных функций для удобства жизни",
        products=[product1, product2, product3]
    )
    # Сбросим счетчики после завершения теста
    reset_category_counts()


@pytest.fixture(scope='function')  # создает новую категорию для каждого теста отдельно
def category2(product4):
    # использование yield в фикстуре позволяет выполнять очистку после завершения теста
    yield Category(
        name="Телевизоры",
        description="Современный телевизор, который позволяет наслаждаться просмотром, "
                    "станет вашим другом и помощником",
        products=[product4]
    )
    # Сбросим счетчики после завершения теста
    reset_category_counts()
