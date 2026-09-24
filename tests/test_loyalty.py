from unittest.mock import Mock

import pytest

from study_project.loyalty import get_discount_percent


@pytest.mark.parametrize(
    ("level", 'expected_cost'),
    [
        ('gold', 15),
        ('silver', 10),
        ('basic', 0)
    ],
)
def test_loyalty_discount(level, expected_cost):
    loyalty_client = Mock()
    loyalty_client.get_level.return_value = level
    sale = get_discount_percent(42, loyalty_client)
    assert sale == expected_cost
    loyalty_client.get_level.assert_called_once_with(42)


def test_connection_error():
    loyalty_client = Mock()
    loyalty_client.get_level.side_effect = ConnectionError('Unlucky')
    sale = get_discount_percent(42, loyalty_client)
    assert sale == 0
    loyalty_client.get_level.assert_called_once_with(42)
