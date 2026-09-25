from unittest.mock import patch

from study_project.invites import generate_invite_code


@patch('study_project.invites.random.randint', return_value=555)
def test_generate_invite_code(mock_randint):
    code = generate_invite_code()
    assert code == 'INV-555'
    mock_randint.assert_called_once_with(100, 999)
