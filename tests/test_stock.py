from unittest.mock import Mock

import pytest

from study_project.stock import reserve_product


@pytest.fixture
def stock_repository():
    return Mock()


@pytest.mark.parametrize(
    ('available', 'quantity'),
    [
        (1, 1),
        (10, 3),
    ]
)
def test_correct_reserve(available, quantity, stock_repository):
    stock_repository.get_available.return_value = available
    product_id = 42
    result = reserve_product(product_id, quantity, stock_repository)
    assert result == "reserved"
    stock_repository.get_available.assert_called_once_with(product_id)
    stock_repository.reserve.assert_called_once_with(product_id, quantity)
