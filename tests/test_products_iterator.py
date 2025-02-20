import pytest


def test_products_iterator(prod_iterator):
    iter(prod_iterator)
    assert prod_iterator.index == 0
    assert next(prod_iterator).name == "Samsung Galaxy S23 Ultra"
    assert next(prod_iterator).name == "Iphone 15"
    assert next(prod_iterator).name == "Xiaomi Redmi Note 11"
    with pytest.raises(StopIteration):
        next(prod_iterator)
