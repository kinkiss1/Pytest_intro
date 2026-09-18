def get_order_status(order_id, payment_client):
    try:
        is_paid = payment_client.is_paid(order_id)
    except ConnectionError:
        return "payment_service_unavailable"

    if is_paid:
        return "ready"
    return "awaiting_payment"


def get_orders_statuses(order_ids, payment_client):
    return [get_order_status(order_id, payment_client) for order_id in order_ids]


def get_paid_order_ids(order_ids, payment_client):
    return [order_id for order_id in order_ids if payment_client.is_paid(order_id)]
