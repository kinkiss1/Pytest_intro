import pytest

from study_project.delivery import get_delivery_cost


@pytest.mark.parametrize(
    ('order_total', 'expected_cost'),
    [(0, 300),
     (2999, 300),
     (3000, 0),
     (3001, 0),
     ],
)
def test_delivery_cost(order_total, expected_cost):
    assert get_delivery_cost(order_total) == expected_cost


def test_delivery_cost_negative():
    with pytest.raises(ValueError, match='отрицательной'):
        get_delivery_cost(-1)


def test_premium_delivery():
    result = get_delivery_cost(100, is_premium=True)
    assert result == 0
