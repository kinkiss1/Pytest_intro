from unittest.mock import Mock

import pytest

from study_project.addresses import add_delivery_address


@pytest.fixture
def address_repository():
    return Mock()


@pytest.mark.parametrize(
    ('user_id', 'address'),
    [
        (1, 'Moscow'),
        (2, 'Kazan'),
    ]
)
def test_address_correct(user_id, address, address_repository):
    address_repository.exists.return_value = False
    result = add_delivery_address(user_id, address, address_repository)
    assert result == 'saved'
    address_repository.save.assert_called_once_with(user_id, address)
    address_repository.exists.assert_called_once_with(user_id, address)


def test_address_is_exists(address_repository):
    address_repository.exists.return_value = True
    result = add_delivery_address(1, 'Moscow', address_repository)
    assert result == 'already_exists'
    address_repository.exists.assert_called_once_with(1, 'Moscow')
    address_repository.save.assert_not_called()


def test_empty_address(address_repository):
    address = ''
    with pytest.raises(ValueError, match='быть пустым'):
        add_delivery_address(1, address, address_repository)
    address_repository.save.assert_not_called()
    address_repository.exists.assert_not_called()
