from unittest.mock import Mock

import pytest

from study_project.registration import register_email


@pytest.mark.parametrize(
    ('correct_email', 'expected_response'),
    [
        ('study@example.com', 'created'),
        ('study2@example.com', 'created'),
    ]
)
def test_correct_email(correct_email, expected_response):
    user_repository = Mock()
    user_repository.is_taken.return_value = False
    result = register_email(correct_email, user_repository)
    assert result == expected_response
    user_repository.is_taken.assert_called_once_with(correct_email)
    user_repository.save.assert_called_once_with(correct_email)


def test_incorrect_email():
    user_repository = Mock()
    user_repository.is_taken.return_value = True
    email = 'study2@example.com'
    result = register_email(email, user_repository)
    assert result == 'email_taken'
    user_repository.is_taken.assert_called_once_with(email)
    user_repository.save.assert_not_called()


def test_incorrect_email2():
    user_repository = Mock()
    email = ''
    with pytest.raises(ValueError, match='пустым'):
        result = register_email(email, user_repository)
    user_repository.is_taken.assert_not_called()
    user_repository.save.assert_not_called()
