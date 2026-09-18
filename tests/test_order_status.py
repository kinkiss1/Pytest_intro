from study_project.order_status import get_paid_order_ids
from unittest.mock import Mock, call

from study_project.order_status import get_order_status, get_orders_statuses


def test_order_status_is_ready_for_paid_order():
    payment_client = Mock()
    payment_client.is_paid.return_value = True

    status = get_order_status(42, payment_client)

    assert status == "ready"
    payment_client.is_paid.assert_called_once_with(42)


def test_order_status_handles_payment_service_error():
    payment_client = Mock()
    payment_client.is_paid.side_effect = ConnectionError("Платёжный сервис недоступен")

    status = get_order_status(42, payment_client)

    assert status == "payment_service_unavailable"
    payment_client.is_paid.assert_called_once_with(42)


def test_order_status_waits_for_unpaid_order():
    payment_client = Mock()
    payment_client.is_paid.return_value = False

    status = get_order_status(42, payment_client)

    assert status == "awaiting_payment"
    payment_client.is_paid.assert_called_once_with(42)


def test_get_orders_statuses_handles_different_payment_responses():
    payment_client = Mock()
    payment_client.is_paid.side_effect = [
        True,
        False,
        ConnectionError("Платежный сервис недоступен"),
    ]
    statuses = get_orders_statuses([101, 102, 103], payment_client)

    assert statuses == [
        "ready",
        "awaiting_payment",
        "payment_service_unavailable",
    ]
    assert payment_client.is_paid.call_args_list == [
        call(101),
        call(102),
        call(103),
    ]


def test_get_paid_order_ids():
    payment_client = Mock()
    payment_client.is_paid.side_effect = [
        True,
        False,
        True,
        False,
    ]
    paid_order_ids = get_paid_order_ids([101, 102, 103, 104], payment_client)
    assert paid_order_ids == [101, 103]
    assert payment_client.is_paid.call_args_list == [
        call(101),
        call(102),
        call(103),
        call(104),
    ]
