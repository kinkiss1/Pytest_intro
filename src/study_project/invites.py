import random


def generate_invite_code():
    number = random.randint(100, 999)
    return f"INV-{number}"
