from unittest.mock import patch

from study_project.coupon import create_coupon


@patch("study_project.coupon.random.randint", return_value=1234)
def test_create_coupon_number(mock_randint):
    coupon = create_coupon()

    assert coupon == "SALE-1234"
    mock_randint.assert_called_once_with(1000, 9999)
