"""Небольшой модуль с функциями для первых тестов."""


def add(first: float, second: float) -> float:
    """Возвращает сумму двух чисел."""
    return first + second


def divide(dividend: float, divisor: float) -> float:
    """Делит dividend на divisor.

    Raises:
        ValueError: если делитель равен нулю.
    """
    if divisor == 0:
        raise ValueError("На ноль делить нельзя")
    return dividend / divisor
