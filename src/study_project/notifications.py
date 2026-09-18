def send_order_notification(email, order_number, client):
    message = f"Заказ №{order_number} оформлен"
    client.send(email, message)
    return message
