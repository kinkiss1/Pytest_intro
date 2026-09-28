def add_delivery_address(user_id, address, addresses_repository):
    if not address:
        raise ValueError("Адрес не может быть пустым")

    if addresses_repository.exists(user_id, address):
        return "already_exists"

    addresses_repository.save(user_id, address)
    return "saved"


def remove_delivery_address(user_id, address, addresses_repository):
    if not addresses_repository.exists(user_id, address):
        return "not_found"

    addresses_repository.delete(user_id, address)
    return "deleted"
