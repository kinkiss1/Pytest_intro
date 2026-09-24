def get_access_level(user_id, permissions_client):
    role = permissions_client.get_role(user_id)

    if role == "admin":
        return "full"

    if role == "manager":
        return "limited"

    return "denied"
