from unittest.mock import Mock

import pytest

from study_project.favorites import add_to_favorites


@pytest.mark.parametrize(
    ('product_id', 'expected_response'),
    [(42, 'added'),
     (100, 'added'),
     ]
)
def test_add_to_favourite(product_id, expected_response):
    favorites_repository = Mock()
    favorites_repository.exists.return_value = False
    result = add_to_favorites(product_id, favorites_repository)
    assert result == expected_response
    favorites_repository.add.assert_called_once_with(product_id)
    favorites_repository.exists.assert_called_once_with(product_id)


def test_add_to_favourite_already_exists():
    favorites_repository = Mock()
    favorites_repository.exists.return_value = True
    ids = 42
    result = add_to_favorites(ids, favorites_repository)
    assert result == "already_in_favorites"
    favorites_repository.add.assert_not_called()
    favorites_repository.exists.assert_called_once_with(ids)


def test_incorrect_ids():
    favorites_repository = Mock()
    ids = 0
    with pytest.raises(ValueError, match='положительным'):
        add_to_favorites(ids, favorites_repository)
    favorites_repository.add.assert_not_called()
    favorites_repository.exists.assert_not_called()
