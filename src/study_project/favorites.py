def add_to_favorites(product_id, favorites_repository):
    if product_id <= 0:
        raise ValueError("ID товара должен быть положительным")

    if favorites_repository.exists(product_id):
        return "already_in_favorites"

    favorites_repository.add(product_id)
    return "added"
