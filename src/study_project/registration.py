def register_email(email, users_repository):
    if not email:
        raise ValueError("Email не может быть пустым")

    if users_repository.is_taken(email):
        return "email_taken"

    users_repository.save(email)
    return "created"
