from doctest import Example
from email import message
from http import client
from unittest.mock import Mock
from study_project.notifications import send_order_notification


def test_send_order_notification_sends_expected_message():
    client = Mock()
    message = send_order_notification(
        "student@example.com",
        42,
        client,
    )
    print("Возвращённое сообщение:", message)
    print("Вызов client.send:", client.send.call_args)
    assert message == "Заказ №42 оформлен"
    client.send.assert_called_once_with("student@example.com", "Заказ №42 оформлен")
