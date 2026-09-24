from re import match
from unittest.mock import Mock, patch, call
from _pytest.fixtures import fixture
import pytest
from study_project.practice import (
    calculate_delivery,
    calculate_average,
    create_reference_code,
    get_user_role,
    get_user_role_safe,
    get_available_order_ids,
)


def test_calculate_delivery():
    assert calculate_delivery(500) == 300


@pytest.mark.parametrize("price", [2_000, 5_000, 10_000])
def test_calculate_delivery_free(price):
    assert calculate_delivery(price) == 0


def test_calculate_delivery_negtive_price():
    with pytest.raises(ValueError, match="отрицательной"):
        calculate_delivery(-1)


@pytest.fixture
def numbers():
    return [10, 20, 30]


def test_calculated_averrage(numbers):
    assert calculate_average(numbers) == 20


def test_calculate_average_empty():
    with pytest.raises(ValueError, match="пустым"):
        calculate_average("")


@patch("study_project.practice.random.randint", return_value=456)
def test_create_reference_code(mock_randint):
    code = create_reference_code()
    assert code == "REF-456"
    mock_randint.assert_called_once_with(100, 999)


def test_get_user_role():
    auth_client = Mock()
    auth_client.fetch_role.return_value = "admin"

    role = get_user_role(7, auth_client)

    assert role == "admin"
    auth_client.fetch_role.assert_called_once_with(7)


def test_get_user_role_safe():
    auth_client = Mock()
    auth_client.fetch_role.side_effect = TimeoutError("Сервис авторизации недоступен")
    role = get_user_role_safe(7, auth_client)
    assert role == "service_unavailable"
    auth_client.fetch_role.assert_called_once_with(7)


def test_get_available_order_ids():
    inventory_client = Mock()
    inventory_client.is_available.side_effect = [True, False, True, False]
    available_order_ids = get_available_order_ids(
        [1, 2, 3, 4],
        inventory_client,
    )
    assert available_order_ids == [1, 3]
    assert inventory_client.is_available.call_args_list == [
        call(1),
        call(2),
        call(3),
        call(4),
    ]
