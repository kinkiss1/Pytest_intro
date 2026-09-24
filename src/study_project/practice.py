import random


def calculate_delivery(price):
    if price < 0:
        raise ValueError("Цена не может быть отрицательной")

    if price >= 2_000:
        return 0

    return 300


def calculate_average(numbers):
    if not numbers:
        raise ValueError("Список не может быть пустым")

    return sum(numbers) / len(numbers)


def create_reference_code():
    return f"REF-{random.randint(100, 999)}"


def get_user_role(user_id, auth_client):
    return auth_client.fetch_role(user_id)


def get_user_role_safe(user_id, auth_client):
    try:
        return auth_client.fetch_role(user_id)
    except TimeoutError:
        return "service_unavailable"


def get_available_order_ids(order_ids, inventory_client):
    return [
        order_id for order_id in order_ids if inventory_client.is_available(order_id)
    ]
