from unittest.mock import Mock, call

import pytest

from study_project.segments import get_user_segment, get_user_segments


@pytest.mark.parametrize(
    ('orders_count', 'exepted_segment'),
    [
        (0, 'new'),
        (1, 'active'),
        (10, 'vip')
    ]
)
def test_segments(orders_count, exepted_segment):
    analytics_client = Mock()
    analytics_client.get_orders_count.return_value = orders_count
    result = get_user_segment(42, analytics_client)
    assert result == exepted_segment
    analytics_client.get_orders_count.assert_called_with(42)


def test_connection_segments():
    analytics_client = Mock()
    analytics_client.get_orders_count.side_effect = ConnectionError('Unlucky')
    result = get_user_segment(42, analytics_client)
    assert result == 'unknown'
    analytics_client.get_orders_count.assert_called_once_with(42)


def test_user_segments_m():
    analytics_client = Mock()
    analytics_client.get_orders_count.side_effect = [0, 1, ConnectionError('not'), 10]
    user_ids = [101, 102, 103, 104]
    result = get_user_segments(user_ids, analytics_client)
    assert result == ['new', 'active', 'unknown', 'vip']
    assert analytics_client.get_orders_count.call_args_list == [
        call(101),
        call(102),
        call(103),
        call(104),
    ]
