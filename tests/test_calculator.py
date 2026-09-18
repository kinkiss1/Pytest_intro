import pytest

from study_project.calculator import add, divide


def test_add_returns_sum():
    assert add(2, 3) == 5


def test_divide_returns_quotient():
    assert divide(10, 2) == 5


def test_divide_by_zero_raises_clear_error():
    with pytest.raises(ValueError, match="ноль"):
        divide(10, 0)
