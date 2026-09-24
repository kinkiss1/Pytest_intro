from unittest.mock import Mock

import pytest

from study_project.welcome import get_welcome_message


@pytest.mark.parametrize(
    ('name', 'expected_message'),
    [
        ('Анна', 'Добро пожаловать, Анна!'),
        (None, 'Пользователь не найден')
    ]
)
def test_welcome(name, expected_message):
    profile_client = Mock()
    profile_client.get_name.return_value = name
    message = get_welcome_message(42, profile_client)
    assert message == expected_message
    profile_client.get_name.assert_called_once_with(42)


def test_connection_message():
    profile_client = Mock()
    profile_client.get_name.side_effect = ConnectionError('Unlucky')
    message = get_welcome_message(42, profile_client)
    assert message == 'Сервис профилей недоступен'
    profile_client.get_name.assert_called_once_with(42)


def test_zero_id():
    profile_client = Mock()
    with pytest.raises(ValueError, match='положительным'):
        get_welcome_message(0, profile_client)
    profile_client.get_name.assert_not_called()
