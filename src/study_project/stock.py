def reserve_product(product_id, quantity, stock_repository):
    if quantity <= 0:
        raise ValueError("Количество должно быть положительным")

    available = stock_repository.get_available(product_id)

    if available < quantity:
        return "not_enough_stock"

    stock_repository.reserve(product_id, quantity)
    return "reserved"
