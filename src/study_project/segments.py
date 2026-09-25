def get_user_segment(user_id, analytics_client):
    try:
        orders_count = analytics_client.get_orders_count(user_id)
    except ConnectionError:
        return "unknown"

    if orders_count >= 10:
        return "vip"

    if orders_count >= 1:
        return "active"

    return "new"


def get_user_segments(user_ids, analytics_client):
    return [
        get_user_segment(user_id, analytics_client)
        for user_id in user_ids
    ]
