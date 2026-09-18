"""Примеры функций с граничными случаями."""


def is_valid_email(value: str) -> bool:
    """Упрощённо проверяет адрес электронной почты.

    Это не полная проверка стандарта e-mail: функция намеренно короткая,
    чтобы было удобно практиковаться в составлении тест-кейсов.
    """
    if not isinstance(value, str) or value.count("@") != 1:
        return False

    local_part, domain = value.split("@")
    return bool(local_part and domain and "." in domain and not domain.startswith("."))
