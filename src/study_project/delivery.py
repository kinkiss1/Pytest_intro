def get_delivery_cost(order_total, is_premium=False):
    if order_total < 0:
        raise ValueError("Сумма заказа не может быть отрицательной")

    if is_premium or order_total >= 3000:
        return 0

    return 300