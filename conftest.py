import pytest
from study_project.shopping_cart import ShoppingCart


@pytest.fixture
def cart():
    new_cart = ShoppingCart()
    new_cart.add_item("Книга", 500)
    return new_cart
