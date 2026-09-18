import pytest


@pytest.mark.parametrize("discount", [-10, 101, 110])
def test_cart_rejects_invalid_discount(cart, discount):
    with pytest.raises(ValueError, match="от 0 до 100"):
        cart.apply_discount(discount)


@pytest.mark.parametrize(
    ("discount", "expected_total"),
    [(0, 500), (10, 450), (50, 250), (100, 0)],
)
def test_cart_calculates_discount(cart, discount, expected_total):
    assert cart.apply_discount(discount) == expected_total


def test_cart_rejects_empty_name(cart):
    with pytest.raises(ValueError, match="пустым"):
        cart.add_item("", 100)


def test_cart_rejects_negative_price(cart):
    with pytest.raises(ValueError, match="отрицательной"):
        cart.add_item("Error", -10)


def test_clear_cart_removes_all_items(cart):
    cart.add_item("something", 100_000)
    cart.clear_cart()
    assert cart.items == []
    assert cart.total() == 0


def test_remove_item_removes_selected_product(cart):
    cart.add_item("pen", 100)
    cart.add_item("notepad", 123)

    cart.remove_item("notepad")

    assert cart.items == [("Книга", 500), ("pen", 100)]
    assert cart.total() == 600


def test_remove_item_rejects_unknown_product(cart):
    with pytest.raises(ValueError, match="не найден"):
        cart.remove_item("mouse")
