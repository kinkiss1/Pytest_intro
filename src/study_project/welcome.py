def get_welcome_message(user_id, profile_client):
    if user_id <= 0:
        raise ValueError("ID пользователя должен быть положительным")

    try:
        name = profile_client.get_name(user_id)
    except ConnectionError:
        return "Сервис профилей недоступен"

    if name is None:
        return "Пользователь не найден"

    return f"Добро пожаловать, {name}!"
