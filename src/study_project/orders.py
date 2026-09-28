def get_user_segment(user_id, analytics_client):
    orders_count = analytics_client.get_orders_count(user_id)

    if orders_count >= 10:
        return "vip"

    if orders_count >= 1:
        return "active"

    return "new"
