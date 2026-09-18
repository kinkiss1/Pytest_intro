import pytest

from study_project.validators import is_valid_email


@pytest.mark.parametrize(
    ("email", "expected"),
    [
        ("student@example.com", True),
        ("name.surname@company.org", True),
        ("without-at-sign.example", False),
        ("@example.com", False),
        ("student@", False),
        ("student@example", False),
    ],
)
def test_is_valid_email(email, expected):
    assert is_valid_email(email) is expected
