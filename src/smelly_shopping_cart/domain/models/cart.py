from smelly_shopping_cart.domain.models.line_item import LineItem
from smelly_shopping_cart.domain.models.product import Product
from smelly_shopping_cart.domain.services.promotion_engine import PromotionEngine


class Cart:
    def __init__(self, id: str, customer_name: str) -> None:  # noqa: A002
        self.id = id
        self.customer_name = customer_name
        self._items: list[LineItem] = []
        self._promotion_engine = PromotionEngine()

    def add_product(self, product: Product, quantity: int = 1) -> None:
        existing = next((item for item in self._items if item.product.equals(product)), None)

        if existing:
            existing.quantity += quantity
        else:
            self._items.append(LineItem(product=product, quantity=quantity))

    @property
    def line_items(self) -> list[LineItem]:
        return self._items

    def calculate_subtotal(self) -> float:
        return self._promotion_engine.apply(self._items)
