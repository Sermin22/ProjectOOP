import pytest


def test_smartphone_product_init(smartphone1):
    """Тест на корректность работы конструктора подкласса Smartphone"""
    assert smartphone1.name == "Samsung Galaxy S23 Ultra"
    assert smartphone1.description == "256GB, Серый цвет, 200MP камера"
    assert smartphone1.price == 180000.0
    assert smartphone1.quantity == 5
    assert smartphone1.efficiency == 95.5
    assert smartphone1.model == "S23 Ultra"
    assert smartphone1.memory == 256
    assert smartphone1.color == "Серый"


def test_smartphone_product_add(smartphone1, smartphone2):
    """Тест на корректность метода сложения продуктов в подклассе Smartphone"""
    smartphone_sum = smartphone1 + smartphone2
    assert smartphone_sum == "Общая стоимость товаров: 2580000.00 руб."


def test_smartphone_product_add_error(smartphone1, grass1):
    """Тест, что функциональность не дает возможности сложить объекты разных классов.
    При попытке сложения разных экземпляров класса или объектов другого типа выбрасывается
    ошибка TypeError"""
    with pytest.raises(TypeError):
        invalid_sum = smartphone1 + grass1
        error_sum = smartphone1 + 1
        assert invalid_sum == "Невозможно сложить объекты разных типов: {type(self)} и {type(other)}."
        assert error_sum == "Невозможно сложить объекты разных типов: {type(self)} и {type(other)}."


def test_lawngrass_product_init(grass1):
    """Тест на корректность работы конструктора подкласса LawnGrass"""
    assert grass1.name == "Газонная трава"
    assert grass1.description == "Элитная трава для газона"
    assert grass1.price == 500.0
    assert grass1.quantity == 20
    assert grass1.country == "Россия"
    assert grass1.germination_period == "7 дней"
    assert grass1.color == "Зеленый"


def test_lawngrass_product_add(grass1, grass2):
    """Тест на корректность метода сложения продуктов в подклассе LawnGrass"""
    grass_sum = grass1 + grass2
    assert grass_sum == "Общая стоимость товаров: 16750.00 руб."


def test_lawngrass_product_add_error(grass1, smartphone1,):
    """Тест, что функциональность не дает возможности сложить объекты разных классов.
    При попытке сложения разных экземпляров класса или объектов другого типа выбрасывается
    ошибка TypeError"""
    with pytest.raises(TypeError):
        invalid_sum = grass1 + smartphone1
        error_sum = grass1 + 1
        assert invalid_sum == "Невозможно сложить объекты разных типов: {type(self)} и {type(other)}."
        assert error_sum == "Невозможно сложить объекты разных типов: {type(self)} и {type(other)}."
