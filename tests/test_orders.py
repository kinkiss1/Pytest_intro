from unittest.mock import Mock

import pytest

from study_project.orders import get_user_segment


@pytest.fixture
def analytics_client():
    return Mock()


@pytest.mark.parametrize(
    ('count', 'return_answer'),
    [
        (0, 'new'),
        (1, 'active'),
        (10, 'vip')

    ]
)
def test_user_segment(analytics_client, count, return_answer):
    analytics_client.get_orders_count.return_value = count
    result = get_user_segment(42, analytics_client)
    assert result == return_answer
    analytics_client.get_orders_count.assert_called_once_with(42)
