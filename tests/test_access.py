from unittest.mock import Mock

import pytest

from study_project.access import get_access_level


@pytest.mark.parametrize(
    ('role', 'expected_access'),
    [
        ('admin', 'full'),
        ('manager', 'limited'),
        ('customer', 'denied'),
    ],
)
def test_get_access_role(role, expected_access):
    permissions_client = Mock()
    permissions_client.get_role.return_value = role
    result = get_access_level(42, permissions_client)
    assert result == expected_access
    permissions_client.get_role.assert_called_once_with(42)
