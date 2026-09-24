def get_discount_percent(user_id, loyalty_client):
    try:
        level = loyalty_client.get_level(user_id)
    except ConnectionError:
        return 0

    if level == "gold":
        return 15

    if level == "silver":
        return 10

    return 0
