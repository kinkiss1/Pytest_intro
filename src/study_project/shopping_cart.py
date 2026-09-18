from dataclasses import dataclass, field


@dataclass
class ShoppingCart:
    """Корзина: хранит товары как пары «название — цена»."""

    items: list[tuple[str, float]] = field(default_factory=list)

    def add_item(self, name: str, price: float) -> None:
        if not name.strip():
            raise ValueError("Название товара не может быть пустым")
        if price < 0:
            raise ValueError("Цена не может быть отрицательной")
        self.items.append((name, price))

    def total(self) -> float:
        return sum(price for _, price in self.items)

    def apply_discount(self, percent: float) -> float:
        if not 0 <= percent <= 100:
            raise ValueError("Скидка должна быть от 0 до 100")
        return self.total() * (1 - percent / 100)

    def clear_cart(self):
        self.items.clear()

    def remove_item(self, name):
        for item in self.items:
            if item[0] == name:
                self.items.remove(item)
                return
        raise ValueError("Товар не найден")
