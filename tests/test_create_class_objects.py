import json
from unittest.mock import mock_open, patch
from src.create_class_objects import read_json, create_objects_from_json
from src.product_and_category import Category, Product


def test_read_json():
    '''Тестирование на вход путь до JSON-файла и возвращает список словарей с данными'''

    # Создаем мок для файла
    mocked_open = mock_open(read_data='[{"name": "Samsung Galaxy C23 Ultra", "price": 180000.0}]')

    # Используем patch для замены вызова open
    with patch('builtins.open', mocked_open):
        # Здесь вызывай свою функцию, которая читает JSON-файл
        result = read_json("../data/products.json")
        assert result == [{"name": "Samsung Galaxy C23 Ultra", "price": 180000.0}]


def test_read_json_another(mock_data):
    '''Тестирование функции чтения JSON-файла'''

    # Преобразуем данные в строку для использования в mock_open
    mock_data_str = json.dumps(mock_data)

    # Маскируем операцию открытия файла
    m = mock_open(read_data=mock_data_str)
    with patch("builtins.open", m):
        # Путь к файлу (в данном случае фиктивный)
        file_path = "../data/products.json"
        result = read_json(file_path)
        expected = mock_data
        assert result == expected


def test_create_objects_from_json(json_data):
    """Тест функции, которая из json-файл создает объекты классов"""

    # Вызываем функцию создания объектов из JSON данных
    categories = create_objects_from_json(json_data)

    # Проверяем количество категорий
    assert len(categories) == 2

    # Проверяем первую категорию
    smartphones_category = categories[0]
    assert isinstance(smartphones_category, Category)
    assert smartphones_category.name == 'Смартфоны'
    assert smartphones_category.description == ('Смартфоны, как средство не только коммуникации, '
                                                'но и получение дополнительных функций для '
                                                'удобства жизни')
    assert len(smartphones_category.products) == 3

    # Проверяем первый продукт первой категории
    samsung_product = smartphones_category.products[0]
    assert isinstance(samsung_product, Product)
    assert samsung_product.name == 'Samsung Galaxy C23 Ultra'
    assert samsung_product.description == '256GB, Серый цвет, 200MP камера'
    assert samsung_product.price == 180000.0
    assert samsung_product.quantity == 5
