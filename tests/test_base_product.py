from unittest.mock import patch
from src.base_product import BaseProduct


def test_base_product_new_product():
    with patch.object(BaseProduct, 'new_product') as mock_new_product:
        # Вызываем метод new_product класса BaseProduct
        result = BaseProduct.new_product("arg1", arg2="value")

        # Проверяем, что был вызван метод new_product базового класса
        mock_new_product.assert_called_once_with("arg1", arg2="value")

        # Проверка результата вызова
        assert result is not None
