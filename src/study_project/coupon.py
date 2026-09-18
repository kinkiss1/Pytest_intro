import random


def create_coupon():
    number = random.randint(1000, 9999)
    return f"SALE-{number}"
